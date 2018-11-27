package us.msu.cse.repair.external.coverage;

import java.io.File;

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

import us.msu.cse.repair.external.util.Util;


public class SeedLineGenerator {
	private static String binJavaDir;
	private static String binTestDir;
	private static Set<String> dependences;
	
	private static Set<String> binJavaClasses;
	private static Set<String> binExecuteTestClasses;
	
	public static void main(String args[]) throws Exception {
		binJavaDir = args[0].trim();
		binTestDir = args[1].trim();
		dependences = new HashSet<String>();
		
		binJavaClasses = new HashSet<String>();
		binExecuteTestClasses = new HashSet<String>();
		
		String[] depStrs = args[2].trim().split(File.pathSeparator);
		for (String dep : depStrs)
			dependences.add(dep);
		
		if (args[3].startsWith("@")) {
			String path = args[3].trim().substring(1);
			List<String> javaLines = Util.readLines(new File(path));
			for (String line : javaLines)
				binJavaClasses.add(line);
		} else {
			String javaClasses[] = args[3].trim().split(File.pathSeparator);
			for (String cls : javaClasses)
				binJavaClasses.add(cls);
		}

		if (args[4].startsWith("@")) {
			String path = args[4].trim().substring(1);
			List<String> testLines = Util.readLines(new File(path));
			for (String line : testLines)
				binExecuteTestClasses.add(line);
		} else {
			String testClasses[] = args[4].trim().split(File.pathSeparator);
			for (String cls : testClasses)
				binExecuteTestClasses.add(cls);
		}	
		
		getSeedLines();
		System.exit(0);
	}
	
	private static void getSeedLines() throws Exception {
		final MemoryClassLoader loader = new MemoryClassLoader(Util.getURLs(binJavaDir, binTestDir, dependences));
		
		final IRuntime runtime = new LoggerRuntime();
		final Instrumenter instr = new Instrumenter(runtime);

		for (String binJavaClass : binJavaClasses) {
			System.out.println(binJavaClass);
			byte[] bytes = instr.instrument(Util.getTargetClass(binJavaDir, binJavaClass), binJavaClass);
			loader.addDefinition(binJavaClass, bytes);
		}

		RuntimeData data = new RuntimeData();
		runtime.startup(data);

		Class<?> targetClasses[] = new Class<?>[binExecuteTestClasses.size()];
		int i = 0;
		for (String testClass : binExecuteTestClasses)
			targetClasses[i++] = loader.loadClass(testClass);

		JUnitCore.runClasses(targetClasses);
		
		final ExecutionDataStore executionData = new ExecutionDataStore();
		final SessionInfoStore sessionInfos = new SessionInfoStore();
		data.collect(executionData, sessionInfos, false);
		runtime.shutdown();

		final CoverageBuilder coverageBuilder = new CoverageBuilder();
		final Analyzer analyzer = new Analyzer(executionData, coverageBuilder);

		
		for (String binJavaClass : binJavaClasses) 
			analyzer.analyzeClass(Util.getTargetClass(binJavaDir, binJavaClass), binJavaClass);

		System.out.println();
		for (final IClassCoverage cc : coverageBuilder.getClasses()) {
			String className = cc.getName().replace("/", ".");
			for (i = cc.getFirstLine(); i <= cc.getLastLine(); i++) {
				int status = cc.getLine(i).getStatus();
				if (status == ICounter.FULLY_COVERED || status == ICounter.PARTLY_COVERED) {
					System.out.println("SeedLine: " + className + "#" + i);
				}
			}
		}
		
		loader.close();
	}
	
	

}
