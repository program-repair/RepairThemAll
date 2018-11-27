package us.msu.cse.repair.external.coverage;

import java.net.URL;
import java.net.URLClassLoader;
import java.util.HashMap;
import java.util.Map;

public class MemoryClassLoader extends URLClassLoader {

	private final Map<String, byte[]> definitions = new HashMap<String, byte[]>();

	public MemoryClassLoader(URL[] urls) {
		super(urls);
		// TODO Auto-generated constructor stub
	}

	public void addDefinition(final String name, final byte[] bytes) {
		definitions.put(name, bytes);
	}

	@Override
	protected Class<?> findClass(final String qualifiedClassName)
			throws ClassNotFoundException {
		byte[] bytes = definitions.get(qualifiedClassName);
		if (bytes != null)
			return defineClass(qualifiedClassName, bytes, 0, bytes.length);

		// Workaround for "feature" in Java 6
		// see http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6434149
		try {
			Class<?> c = Class.forName(qualifiedClassName);
			return c;
		} catch (ClassNotFoundException nf) {
			// Ignore and fall through
		}
		return super.findClass(qualifiedClassName);
	}
}