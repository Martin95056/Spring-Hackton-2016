package CardLogic;

public class PairValues {

	private int trumpValue;
	private int nonTrumpValue;

	public PairValues(int trumpValue, int nonTrumpValue) {
		super();
		this.trumpValue = trumpValue;
		this.nonTrumpValue = nonTrumpValue;
	}

	public int getTrumpValue() {
		return trumpValue;
	}

	public int getNonTrumpValue() {
		return nonTrumpValue;
	}

}
