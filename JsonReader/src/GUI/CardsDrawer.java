package GUI;

import java.awt.Dimension;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import CardLogic.Card;

public class CardsDrawer {

	private JFrame frame;
	private int drawX, drawY;
	private int cardWidth, cardHeigth;
	private int centralDrawWidth, centralDrawHeigth;
	private JPanel contentPane;
	private JLabel currentLabel = null;
	private static CardsDrawer instance = null;

	private CardsDrawer() {

		frame = new JFrame("ProBelot");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		cardWidth = (int) screenSize.getWidth() / 15;
		cardHeigth = (int) screenSize.getHeight() / 8;
		drawX = cardWidth * 2;
		drawY = (int) screenSize.getHeight() - cardHeigth - 30;
		centralDrawWidth = drawX + (int) 3.7 * cardWidth + 50;
		centralDrawHeigth = (int) (drawY - 1.5 * cardHeigth - 30);
		contentPane = new JPanel();
		frame.setContentPane(contentPane);
		frame.setLocationByPlatform(true);
		frame.setVisible(true);
	}

	public static CardsDrawer getInstance() {
		if (instance == null) {
			instance = new CardsDrawer();
		}
		return instance;
	}

	public void drawCards(ArrayList<Card> cards) {
		for (Card c : cards) {
			DrawCard(c);
		}
	}

	private void DrawCard(Card card) {
		final JButton button;
		ImageIcon image = null;
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		try {
			File imageFile = new File(
					"/home/misho/HackBulgaria-Programming101/ProBelot/Spring-Hackton-2016/card-BMPs/"
							+ card.getValue() + card.getSuit() + ".bmp");
			image = new ImageIcon(ImageIO.read(imageFile).getScaledInstance(
					cardWidth, cardHeigth, Image.SCALE_SMOOTH));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		button = new JButton(image);
		button.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				button.setVisible(false);
				contentPane.remove(button);
				if (currentLabel != null) {
					currentLabel.setVisible(false);
					contentPane.remove(currentLabel);
				}

				JLabel picLabel = new JLabel(button.getIcon());
				picLabel.setBounds(centralDrawWidth, centralDrawHeigth,
						cardWidth, cardHeigth);
				picLabel.setVisible(true);
				contentPane.add(picLabel);
				currentLabel = picLabel;
				frame.pack();

			}

		});
		button.setName(card.getValue() + card.getSuit());
		button.setBounds(drawX, drawY, cardWidth, cardHeigth);
		contentPane.setLayout(null);
		contentPane.add(button);
		frame.pack();
		drawX += cardWidth + 15;
	}
}
