package us.msu.cse.repair.external.coverage;

public class LCNode {
	String className;
	int lineNumber;

	public LCNode(String className, int lineNumber) {
		this.className = className;
		this.lineNumber = lineNumber;
	}

	public String getClassName() {
		return className;
	}

	public int getLineNumber() {
		return lineNumber;
	}

	public void setClassName(String className) {
		this.className = className;
	}

	public void setLineNumber(int lineNumber) {
		this.lineNumber = lineNumber;
	}

	@Override
	public boolean equals(Object o) {
		if (!(o instanceof LCNode))
			return false;
		LCNode node = (LCNode) o;
		String a = this.className + "#" + this.lineNumber;
		String b = node.className + "#" + node.lineNumber;
		return a.equals(b);
	}

	@Override
	public int hashCode() {
		String a = this.className + "#" + this.lineNumber;
		return a.hashCode();
	}

	@Override
	public String toString() {
		return this.className + "#" + this.lineNumber;
	}
}
