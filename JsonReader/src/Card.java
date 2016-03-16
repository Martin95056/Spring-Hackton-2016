public class Card {
	private String value;
	private String suit;
	private int trumpValue;
	private int nonTrumpValue;

	public Card(String value, String suit, int trumpValue, int nonTrumpValue) {
		super();
		this.value = value;
		this.suit = suit;
		this.trumpValue = trumpValue;
		this.nonTrumpValue = nonTrumpValue;
		
	}

	public int getTrumpValue() {
		return trumpValue;
	}

	public int getNonTrumpValue() {
		return nonTrumpValue;
	}

	public String getValue() {
		return value;
	}

	public String getSuit() {
		return suit;
	}
	
	@Override
	public String toString()
	{
		return value + " of " + suit;
	}


}