package us.msu.cse.repair.external.coverage;

import java.io.File;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.jacoco.core.analysis.Analyzer;
import org.jacoco.core.analysis.CoverageBuilder;
import org.jacoco.core.analysis.IClassCoverage;
import org.jacoco.core.analysis.ICounter;
import org.jacoco.core.data.ExecutionDataStore;
import org.jacoco.core.data.SessionInfoStore;
import org.jacoco.core.instr.Instrumenter;
import org.jacoco.core.runtime.IRuntime;
import org.jacoco.core.runtime.LoggerRuntime;
import org.jacoco.core.runtime.RuntimeData;
import org.junit.runner.JUnitCore;
import org.junit.runner.Request;

import us.msu.cse.repair.external.util.Util;

public class TestFilter2 {
	private static String binJavaDir;
	private static String binTestDir;
	private static Set<String> dependences;
	
	private static Set<String> allTests;
	private static Set<String> analyzedClasses;
	
	public static void main(String args[]) throws Exception {
		binJavaDir = args[0].trim();
		binTestDir = args[1].trim();
		dependences = new HashSet<String>();
		
		analyzedClasses = new HashSet<String>();
		allTests = new HashSet<String>();
		
		String depStrs[] = args[2].trim().split(File.pathSeparator);
		for (String dep : depStrs)
			dependences.add(dep);
		
		String acStrs[] = args[3].trim().split(File.pathSeparator);
		for (String ac : acStrs)
			analyzedClasses.add(ac);
		
		
		if (args[4].startsWith("@")) {
			String path = args[4].trim().substring(1);
			List<String> lineStrs = Util.readLines(new File(path));
			for (String str : lineStrs)
				allTests.add(str.trim());
		} else {
			String tStrs[] = args[4].trim().split(File.pathSeparator);
			for (String str : tStrs)
				allTests.add(str);
		}
		
		List<String> filteredTests = getFilteredTests();
		printFilteredTests(filteredTests);
		System.exit(0);
	}
	
	private static void printFilteredTests(List<String> filteredTests) {
		System.out.println();
		for (String test : filteredTests)
			System.out.println("FilteredTest: " + test);
	}
	
	
	private static List<String> getFilteredTests() throws Exception {
		List<String> filteredTests = new ArrayList<String>();
		for (String test : allTests) {
			if (!canFiltered(test))
				filteredTests.add(test);
		}

		return filteredTests;
	}

	private static boolean canFiltered(String test)
			throws Exception {
		final MemoryClassLoader loader = new MemoryClassLoader(Util.getURLs(binJavaDir, binTestDir, dependences));
		
		final IRuntime runtime = new LoggerRuntime();
		final Instrumenter instr = new Instrumenter(runtime);

		for (String binJavaClass : analyzedClasses) {
			InputStream istream = Util.getTargetClass(binJavaDir, binJavaClass);
			byte[] bytes = instr.instrument(istream, binJavaClass);
			istream.close();
			loader.addDefinition(binJavaClass, bytes);
		}

		RuntimeData data = new RuntimeData();
		runtime.startup(data);

		String clsName = test.split("#")[0];
		String mName = test.split("#")[1];
		Request request = Request.method(loader.loadClass(clsName), mName);
		new JUnitCore().run(request);		

		final ExecutionDataStore executionData = new ExecutionDataStore();
		final SessionInfoStore sessionInfos = new SessionInfoStore();
		data.collect(executionData, sessionInfos, false);
		runtime.shutdown();

		final CoverageBuilder coverageBuilder = new CoverageBuilder();
		final Analyzer analyzer = new Analyzer(executionData, coverageBuilder);

		for (String binJavaClass : analyzedClasses) {
			InputStream istream = Util.getTargetClass(binJavaDir, binJavaClass);
			analyzer.analyzeClass(istream, binJavaClass);
			istream.close();
		}

		loader.close();
		
		for (final IClassCoverage cc : coverageBuilder.getClasses()) {
			for (int i = cc.getFirstLine(); i <= cc.getLastLine(); i++) {
				int status = cc.getLine(i).getStatus();
				if (status == ICounter.FULLY_COVERED || status == ICounter.PARTLY_COVERED) 
					return false;
			}
		}
		
		return true;
	}
}
