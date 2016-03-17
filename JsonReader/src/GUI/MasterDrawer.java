package GUI;

import java.io.File;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JPanel;

import CardLogic.Card;
import CardLogic.JsonParser;

public class MasterDrawer {

	private JFrame frame;
	private JPanel contentPanel;
	private ArrayList<Card> playerCards;
	private PlayerCardsDrawer playerCardsDrawer = null;
	private BotCardsDrawer botCardsDrawer = null;

	MasterDrawer() {
		contentPanel = new JPanel();
		contentPanel.setLayout(null);
		frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
		frame.setContentPane(contentPanel);
		frame.setLocationByPlatform(true);
		frame.setVisible(true);
		playerCardsDrawer = new PlayerCardsDrawer(frame, contentPanel);
		botCardsDrawer = new BotCardsDrawer(frame, contentPanel);
	}

	private void readFirstFivePlayerCards(File playerCardsFile) {
		playerCards = JsonParser.getFirst5CardsFromJson(playerCardsFile);
	}

	public void drawPlayerCards() {
		ArrayList<Card> cards = new ArrayList<Card> ();
		cards.add(new Card("A", "Clubs"));
		cards.add(new Card("J", "Clubs"));
		cards.add(new Card("9", "Clubs"));
	    cards.add(new Card("10", "Clubs"));
	    cards.add(new Card("8", "Clubs"));
        cards.add(new Card("Q", "Clubs"));
	    cards.add(new Card("K", "Clubs"));
	    cards.add(new Card("7", "Clubs"));
	    playerCardsDrawer.drawCards(cards);
		//playerCardsDrawer.drawCards(playerCards);
	}
	
	public void drawBotCards()
	{
		botCardsDrawer.drawTopBotCards(8);
		botCardsDrawer.drawLeftBotCards(8);
		botCardsDrawer.drawRightBotCards(8);
	}

}
