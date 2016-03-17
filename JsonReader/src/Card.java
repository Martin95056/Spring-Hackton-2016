
public class Card {
	private String value;
	private String suit;
	PairValues pairValues;

	public Card(String value, String suit) {
		super();
		this.value = value;
		this.suit = suit;
		pairValues = CardPairValues.getInstance().getMap().get(value);

	}

	public int getTrumpValue() {
		return pairValues.getTrumpValue();
	}

	public int getNonTrumpValue() {
		return pairValues.getNonTrumpValue();
	}

	public String getValue() {
		return value;
	}

	public String getSuit() {
		return suit;
	}

	@Override
	public String toString() {
		return value + " of " + suit;
	}

	@Override
	public boolean equals(Object card) {
		if (card == null)
			return false;
		if (!(card instanceof Card))
			return false;
		Card cast = (Card) card;
		if (cast.getSuit() == suit && cast.getValue() == value)
			return true;
		else
			return false;
	}

}
