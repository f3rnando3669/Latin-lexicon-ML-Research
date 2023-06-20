package NLP.Software.Pipeline;

import edu.stanford.nlp.io.EncodingPrintWriter;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import org.example.Example.Pipeline;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner;

public class NLP_Software {

    public static StanfordCoreNLP stanfordCoreNLP = Pipeline.getPipeline();

    public static void main(String[] args) throws FileNotFoundException {

        // Scanner reads from input.txt
        Scanner scanner = new Scanner(new File("C://Users//sansk//IdeaProjects//Example//src//main//java//NLP//Software//Pipeline//input.txt"));

        // Creates an output.txt file to return outputs to
        PrintWriter out = new PrintWriter("C://Users//sansk//IdeaProjects//Example//src//main//java//NLP//Software//Pipeline//output.txt");

        while (scanner.hasNextLine()) {
            // Reads each line of input
            String input = scanner.nextLine();

            // Gives back a count for array size for each sentence
            int array_count = countWords(input);

            // Gives each line to the lemma method.
            String lemma_output = Lemma(input, array_count);

            out.println(lemma_output);

            //System.out.println(input);
        }

        scanner.close();
        out.close();

    }

    // Function to count total number of words in the string
    public static int countWords(String input)
    {

        // Check if the string is null or empty then return zero
        if (input == null || input.isEmpty()) {
            return 0;
        }

        // Splitting the string around matches of the given regular expression
        // s is a special character in regular expressions that represents whitespace.
        String[] words = input.split("[\\s.]+");

        // Check if the last character is a dot, and if so, increment the word count
        if (input.trim().endsWith(".")) {
            return words.length + 1;
        }

        // Return number of words in the given string
        return words.length;
    }

    // Takes a string as an input
    // Return the same string but lemmatized
    public static String Lemma(String input, int array_length) {

        String[] words = new String[array_length + 2];

        CoreDocument coreDocument = new CoreDocument(input);

        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();

        String lemma = "";

        int i = 0;
        for (CoreLabel coreLabel : coreLabelList) {

            words[i] = coreLabel.lemma();
            i++;

        }
        String output = String.join(" ", words);
        return output;
    }

    public static String POS(String lemma_output) {

        return lemma_output;
    }

    public static void PatternCheck() {
        return;
    }


}
