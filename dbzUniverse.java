import java.util.HashMap;

public class dbzUniverse {
    public static void main(String[] args) {
        // Create a Mapping of Characters and Life Energy
        HashMap<String, int[]> characterPosters = new HashMap <> ();

        characterPosters.put("Beerus", new int[]{7784,7897,7451,3658});
        characterPosters.put("Goku", new int[]{5644,7855,2215,7844});
        characterPosters.put("Whis", new int[]{9899,8774,9855,8552});
        characterPosters.put("Vegeta", new int[]{10565,9877,8966,8877});

        for (String character:characterPosters.keySet()) {
            System.out.print(character + ": ");
            int[] posters = characterPosters.get(character);
            for (int poster: posters) {
                System.out.print(poster + " : ");

            }
            System.out.println();
        }
    }
}
