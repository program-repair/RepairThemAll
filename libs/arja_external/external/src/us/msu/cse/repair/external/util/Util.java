package us.msu.cse.repair.external.util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class Util {
	public static InputStream getTargetClass(String dir, final String name) throws FileNotFoundException {
		final String resource = name.replace('.', '/') + ".class";
		File file = new File(dir, resource);
		return new FileInputStream(file);
	}
	
	public static URL[] getURLs(String binJavaDir, String binTestDir, Set<String> dependences)
			throws MalformedURLException {
		URL[] urls = new URL[dependences.size() + 2];
		urls[0] = new File(binJavaDir).toURI().toURL();
		urls[1] = new File(binTestDir).toURI().toURL();
		int i = 2;
		for (String dep : dependences)
			urls[i++] = new File(dep).toURI().toURL();
		return urls;
	}
	
	public static List<String> readLines(File file) throws IOException {
		FileInputStream fstream = new FileInputStream(file);
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

		String strLine;
		List<String> lines = new ArrayList<String>();
		while ((strLine = br.readLine()) != null)  
			lines.add(strLine.trim());
		br.close();
		return lines;
	}
}
