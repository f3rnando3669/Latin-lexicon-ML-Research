package NLP_Pipeline;

import com.robbinstony.nlp.Pipeline;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;

public class NLP_Pipeline {
    public static StanfordCoreNLP stanfordCoreNLP = Pipeline.getPipeline();

    public static void main(String[] args) throws FileNotFoundException {

        Scanner scanner = new Scanner(new File("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//input.txt"));

        PrintWriter out = new PrintWriter("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//output.txt");

        while (scanner.hasNextLine()) {
            // Reads each line of input
            String input = scanner.nextLine();

            // Separate the sentences
            String[] sentences = seperatedSentences(input);

            // Process each sentence individually
            for (String sentence : sentences) {
                // Declare a variable to store the formatted HashMap contents exclusive to each sentence
                StringBuilder HashMapOutput = new StringBuilder();

                StringBuilder IndexMapOutput = new StringBuilder();

                // Lemmatize the sentence
                String lemmaOutput = Lemma(sentence);

                // Perform Part-of-Speech tagging on the lemmatized sentence
                String posOutput = POS(lemmaOutput);

                Map<Integer, String> indexmap = IndexPoSConnect(posOutput);

                // Check for specific patterns in the Part-of-Speech tags
                String patternMatchedOutput = PatternCheck(indexmap);

                // Convert the pattern string to an array
                String[] patternArray = PatternToArray(patternMatchedOutput);

                // Connect lemmas and POS tags into a map
                Map<String, String> wordMap = ConnectLemmaPOS(lemmaOutput, posOutput);

                // Find matched words based on the patterns and word map
                String wordMatch = MatchedWords(patternArray, wordMap);

                // Append each key-value pair from the word map to HashMapOutput
                for (Map.Entry<String, String> entry : wordMap.entrySet()) {
                    HashMapOutput.append(entry.getKey()).append(" -> ").append(entry.getValue()).append("\n");
                }

                for (Map.Entry<Integer, String> entry : indexmap.entrySet()) {
                    IndexMapOutput.append(entry.getKey()).append(" -> ").append(entry.getValue()).append("\n");
                }

                // Write the results to the output file
                out.println("Input: " + sentence + "\nPost-Lemma: " + lemmaOutput + "\nPost-POS: " + posOutput + "\nPattern Matching: " + patternMatchedOutput + "\nIndexMapOutput\n" + IndexMapOutput + "\nConnect Output:\n" + HashMapOutput + "Matched Words: " + wordMatch + "\n");

                // If you want to write the separated sentences to a file, uncomment the following line:
                // out.println(separatedSentences(lemmaOutput));
            }
        }
        scanner.close();
        out.close();
    }

    // Separate input into sentences
    public static String[] seperatedSentences(String input) {
        // (\\.) or a question mark (\\?) but doesn't include the period
        // or question mark in the match. This allows the split to occur
        // after a period or question mark without consuming them.
        return input.split("(?<=[.?])\\s+");
        // \\s+ matches one or more whitespace characters
        // (spaces, tabs, newlines) immediately after the period or question mark.
    }

    // Lemmatize the input string
    public static String Lemma(String input) {
        CoreDocument coreDocument = new CoreDocument(input);
        stanfordCoreNLP.annotate(coreDocument);
        List<CoreLabel> coreLabelList = coreDocument.tokens();
        String[] words = new String[coreLabelList.size()];
        int i = 0;
        for (CoreLabel coreLabel : coreLabelList) {
            words[i] = coreLabel.lemma();
            i++;
        }
        return String.join(" ", words);
    }

    // Perform Part-of-Speech tagging on the input string
    public static String POS(String lemmaOutput) {
        CoreDocument coreDocument = new CoreDocument(lemmaOutput);
        stanfordCoreNLP.annotate(coreDocument);
        List<CoreLabel> coreLabelList = coreDocument.tokens();
        String[] words = new String[coreLabelList.size()];
        int i = 0;
        for (CoreLabel coreLabel : coreLabelList) {
            words[i] = coreLabel.get(CoreAnnotations.PartOfSpeechAnnotation.class);
            i++;
        }
        return String.join(" ", words);
    }

    public static Map<Integer, String> IndexPoSConnect(String posOutput) {
        String[] posWords = splitIntoWords(posOutput);

        Map<Integer, String> indexmap = new LinkedHashMap<>();

        for (int i = 0; i < posWords.length; i++) {
            String value = posWords[i];

            indexmap.put(i, value);
        }

        return indexmap;
    }

    // Check for specific patterns in the Part-of-Speech tags
    public static String PatternCheck(Map<Integer, String> indexMap) {
        // Check if the indexMap matches Pattern X
        if (isPattern1(indexMap)) {
            return "DT NN VBP NN"; // Return the matched pattern
        } else if (isPattern2(indexMap)) {
            return "DT NN VB NN";
        } else if (isPattern3(indexMap)) {
            return "DT NN VBP JJ";
        }else if (isPattern4(indexMap)) {
            return "DT NN VB JJ";
        }else if (isPattern5(indexMap)) {
            return "NNP VBP NN";
        }else if (isPattern6(indexMap)) {
            return "NNP VB NN";
        }else if (isPattern7(indexMap)) {
            return "NNP VBP JJ";
        }else if (isPattern8(indexMap)) {
            return "NNP VB JJ";
        }else if (isPattern9(indexMap)) {
            return "NN VBP NN";
        }else if (isPattern10(indexMap)) {
            return "NN VB NN";
        }else if (isPattern11(indexMap)) {
            return "NN VBP JJ";
        }else if (isPattern12(indexMap)) {
            return "NN VB JJ";
        }else { // If neither pattern is found
            return "Pattern Not Found"; // Return the "Pattern Not Found" message
        }
    }

    private static boolean isPattern1(Map<Integer, String> indexMap) {
        // Get the indices for each value in Pattern 1
        int dtIndex = getIndexForValue(indexMap, "DT");
        int nnIndex = getIndexAfterValue(indexMap, dtIndex, "NN");
        int vbpIndex = getIndexAfterValue(indexMap, nnIndex, "VBP");
        int nn2Index = getIndexAfterValue(indexMap, vbpIndex, "NN");

        // Check if all indices are found in the expected order
        return dtIndex != -1 && nnIndex != -1 && vbpIndex != -1 && nn2Index != -1;
    }

    private static boolean isPattern2(Map<Integer, String> indexMap) {
        // Get the indices for each value in Pattern 2
        int dtIndex = getIndexForValue(indexMap, "DT");
        int nnIndex = getIndexAfterValue(indexMap, dtIndex, "NN");
        int vbIndex = getIndexAfterValue(indexMap, nnIndex, "VB");
        int nn2Index = getIndexAfterValue(indexMap, vbIndex, "NN");

        // Check if all indices are found in the expected order
        return dtIndex != -1 && nnIndex != -1 && vbIndex != -1 && nn2Index != -1;
    }

    private static boolean isPattern3(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int dtIndex = getIndexForValue(indexMap, "DT");
        int nnIndex = getIndexAfterValue(indexMap, dtIndex, "NN");
        int vbpIndex = getIndexAfterValue(indexMap, nnIndex, "VBP");
        int jjIndex = getIndexAfterValue(indexMap, vbpIndex, "JJ");

        // Check if all indices are found in the expected order
        return dtIndex != -1 && nnIndex != -1 && vbpIndex != -1 && jjIndex != -1;
    }

    private static boolean isPattern4(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int dtIndex = getIndexForValue(indexMap, "DT");
        int nnIndex = getIndexAfterValue(indexMap, dtIndex, "NN");
        int vbIndex = getIndexAfterValue(indexMap, nnIndex, "VB");
        int jjIndex = getIndexAfterValue(indexMap, vbIndex, "JJ");

        // Check if all indices are found in the expected order
        return dtIndex != -1 && nnIndex != -1 && vbIndex != -1 && jjIndex != -1;
    }

    private static boolean isPattern5(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int nnpIndex = getIndexForValue(indexMap, "NNP");
        int vbpIndex = getIndexAfterValue(indexMap, nnpIndex, "VBP");
        int nnIndex = getIndexAfterValue(indexMap, vbpIndex, "NN");

        // Check if all indices are found in the expected order
        return nnpIndex != -1 && vbpIndex != -1 && nnIndex != -1;
    }

    private static boolean isPattern6(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int nnpIndex = getIndexForValue(indexMap, "NNP");
        int vbIndex = getIndexAfterValue(indexMap, nnpIndex, "VB");
        int nnIndex = getIndexAfterValue(indexMap, vbIndex, "nn");

        // Check if all indices are found in the expected order
        return nnpIndex != -1 && vbIndex != -1 && nnIndex != -1;
    }

    private static boolean isPattern7(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int nnpIndex = getIndexForValue(indexMap, "NNP");
        int vbpIndex = getIndexAfterValue(indexMap, nnpIndex, "VBP");
        int jjIndex = getIndexAfterValue(indexMap, vbpIndex, "JJ");

        // Check if all indices are found in the expected order
        return nnpIndex != -1 && vbpIndex != -1 && jjIndex != -1;
    }

    private static boolean isPattern8(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int nnpIndex = getIndexForValue(indexMap, "NNP");
        int vbIndex = getIndexAfterValue(indexMap, nnpIndex, "VB");
        int jjIndex = getIndexAfterValue(indexMap, vbIndex, "JJ");

        // Check if all indices are found in the expected order
        return nnpIndex != -1 && vbIndex != -1 && jjIndex != -1;
    }

    private static boolean isPattern9(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int nnIndex = getIndexForValue(indexMap, "NN");
        int vbpIndex = getIndexAfterValue(indexMap, nnIndex, "VBP");
        int nn2Index = getIndexAfterValue(indexMap, vbpIndex, "NN");

        // Check if all indices are found in the expected order
        return nnIndex != -1 && vbpIndex != -1 && nn2Index != -1;
    }

    private static boolean isPattern10(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int nnIndex = getIndexForValue(indexMap, "NN");
        int vbIndex = getIndexAfterValue(indexMap, nnIndex, "VB");
        int nn2Index = getIndexAfterValue(indexMap, vbIndex, "NN");

        // Check if all indices are found in the expected order
        return nnIndex != -1 && vbIndex != -1 && nn2Index != -1;
    }

    private static boolean isPattern11(Map<Integer, String> indexMap){
        // Get the indices for each value in Pattern 1
        int nnIndex = getIndexForValue(indexMap, "NN");
        int vbpIndex = getIndexAfterValue(indexMap, nnIndex, "VBP");
        int jjIndex = getIndexAfterValue(indexMap, vbpIndex, "JJ");

        // Check if all indices are found in the expected order
        return nnIndex != -1 && vbpIndex != -1 && jjIndex != -1;
    }

    private static boolean isPattern12(Map<Integer, String> indexMap){
// Get the indices for each value in Pattern 1
        int nnIndex = getIndexForValue(indexMap, "NN");
        int vbpIndex = getIndexAfterValue(indexMap, nnIndex, "VBP");
        int jjIndex = getIndexAfterValue(indexMap, vbpIndex, "JJ");

        // Check if all indices are found in the expected order
        return nnIndex != -1 && vbpIndex != -1 && jjIndex != -1;
    }

    private static int getIndexForValue(Map<Integer, String> indexMap, String value) {
        // Iterate over the indexMap to find the index of the specified value
        for (Map.Entry<Integer, String> entry : indexMap.entrySet()) {
            if (entry.getValue().equals(value)) {
                //System.out.println("Value '" + value + "' is found at index " + entry.getKey() + ".");
                return entry.getKey(); // Return the index if the value is found
            }
        }
        return -1; // Return -1 if the value is not found
    }

    private static int getIndexAfterValue(Map<Integer, String> indexMap, int startIndex, String value) {
        // Iterate over the indexMap to find the index of the specified value occurring after the startIndex
        for (Map.Entry<Integer, String> entry : indexMap.entrySet()) {
            int currentIndex = entry.getKey();
            String currentValue = entry.getValue();

            if (currentIndex > startIndex && currentValue.equals(value)) {
                //System.out.println("Value '" + value + "' is found after index " + startIndex + " at index " + currentIndex + ".");
                return currentIndex; // Return the index if the value is found after the startIndex
            }
        }
        return -1; // Return -1 if the value is not found or found before the startIndex
    }

    // Split a sentence into individual words
    public static String[] splitIntoWords(String sentence) {
        return sentence.split("\\s+");
    }

    // Connect lemmas and POS tags into a map
    public static Map<String, String> ConnectLemmaPOS(String lemmaInput, String posOutput) {
        String[] lemmaWords = splitIntoWords(lemmaInput);
        String[] posWords = splitIntoWords(posOutput);

        // Create a LinkedHashMap to store the mapping of lemmaWords to posWords
        Map<String, String> wordMap = new LinkedHashMap<>();

        // Iterate over the arrays and put the elements into the LinkedHashMap
        for (int i = 0; i < lemmaWords.length; i++) {
            String lemma = lemmaWords[i];
            String pos = i + ". " + posWords[i];

            // Generate a unique key for each word by appending its index
            String key = i + ". " + lemma;

            // Put the word and its corresponding POS tag into the map
            wordMap.put(pos, key);
        }

        // Returning the LinkedHashMap
        return wordMap;
    }

    // Convert pattern string to an array of words
    public static String[] PatternToArray(String patternOutput) {
        return splitIntoWords(patternOutput);
    }

    // Find matched words based on patterns and word map
    public static String MatchedWords(String[] pattern, Map<String, String> wordMap) {
        StringBuilder matchedWords = new StringBuilder();

        // Iterate over the pattern array
        for (String patternWord : pattern) {
            // Iterate over the wordMap entries
            for (Map.Entry<String, String> entry : wordMap.entrySet()) {
                if (entry.getValue().equals(patternWord)) {
                    // Append the matching key to the matchedWords StringBuilder
                    matchedWords.append(entry.getKey()).append(" ");

                    break; // Break the inner loop to move to the next pattern word
                }
            }
        }

        return matchedWords.toString().trim(); // Trim any trailing whitespace and return the result
    }
}
