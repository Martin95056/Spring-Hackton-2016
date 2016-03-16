import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class JsonParser {
	public static ArrayList<?> getFirst5CardsFromJson(File file){
			ArrayList<Map.Entry<String,String> > cardsArray=null;
		try {
			BufferedReader reader=new BufferedReader(new FileReader(file));
			//System.out.println(file);
			String line=null;
			StringBuilder input=new StringBuilder();
			while((line=reader.readLine())!=null){
				input.append(line);
			}
			reader.close();
			JSONObject jsonObject = new JSONObject(input.toString());
			String contract= (String) jsonObject.get("contract");
			System.out.println(contract);
			JSONArray cards = jsonObject.getJSONArray("cards");
			//Iterator<String> iterator = msg.iterator();
			cardsArray=new ArrayList<>();
			 int size = cards.length();
			    for (int i = 0; i < size; i++) {
			        JSONObject another_json_object =  cards.getJSONObject(i);
			           
			            JSONObject jsonObject2 = new JSONObject(another_json_object.toString());
			            System.out.println(jsonObject2.get("value").toString()+" "+jsonObject2.get("suit"));
			            cardsArray.add(new java.util.AbstractMap.SimpleEntry(jsonObject2.get("value"), jsonObject2.get("suit")));
			    }


		} catch (JSONException e) {
			e.printStackTrace();
		} catch(IOException e){
			e.printStackTrace();
		}
		
	     return cardsArray;
	}
}
