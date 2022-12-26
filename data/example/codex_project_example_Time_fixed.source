protected BasePeriod(long duration) {
    super();
    // bug [3264409]
    iType = PeriodType.time();
    int[] values = ISOChronology.getInstanceUTC().get(this, duration);
    iType = PeriodType.standard();
    iValues = new int[8];
    System.arraycopy(values, 0, iValues, 4, 4);
}