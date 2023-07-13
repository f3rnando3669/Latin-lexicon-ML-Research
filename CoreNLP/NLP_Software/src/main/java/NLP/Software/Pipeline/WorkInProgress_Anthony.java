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

public class NLP_Pipeline_Nested_Ifs {
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

                // Check for specific patterns in the Part-of-Speech tags
                String patternMatchedOutput = PatternCheck(posOutput);

                // Convert the pattern string to an array
                String[] patternArray = PatternToArray(patternMatchedOutput);

                Map<Integer, String> indexmap = IndexPoSConnect(posOutput);

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
                out.println("Input: " + sentence + "\nPost-Lemma: " + lemmaOutput + "\nPost-POS: " + posOutput + "\nPattern Matching: " + patternMatchedOutput + "\n\nIndexMapOutput\n" + IndexMapOutput + "\nConnect Output:\n" + HashMapOutput + "\nMatched Words: " + wordMatch + "\n");

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
    public static String PatternCheck(String POSoutput) {

        String[] myArray = new String[]{"DT", "NN", "VBP", "NN"};

        // -------------------------------------------------------------------------------------------------------------
        // Check if VBP exists, if it does store its index.
        boolean is_VBP = isPresent(myArray, "VBP");
        int VBP_index = 0;
        if(is_VBP){
            VBP_index = locIndex(myArray, "VBP");
            System.out.println("VBP exists in the array at: " + VBP_index);
        }

        // Check if DT exists, if it does store its index and look for an NN with an index between DT and VBP.
        // If such an index exists, call it NN1_index.
        boolean is_DT = isPresent(myArray, "DT");
        int DT_index = 0;
        int NN1_index = 0;
        if(is_DT){
            DT_index = locIndex(myArray, "DT");
            System.out.println("DT exists at: " + DT_index);
            boolean is_NN = isPresent(myArray, "NN");
            if(is_NN){
                int NN_index = locIndex(myArray, "NN");
                if(NN_index > DT_index && NN_index < VBP_index){
                    NN1_index = NN_index;
                    System.out.println("An instance of NN exists after DT (" + DT_index + ") and before VBP (" + VBP_index + ") at: " + NN1_index);
                }
            }
        }

        // Since DT does not exist, check if an NN exists with an index less than VBP, if so, call it NN2.
        int NN2_index = 0;
        if(!is_DT) {
            boolean is_NN = isPresent(myArray, "NN");
            if (is_NN) {
                int NN_index = locIndex(myArray, "NN");
                if (NN_index < VBP_index) {
                    NN2_index = NN_index;
                    System.out.println("NN exists at: " + NN2_index + " which is before VBP at: " + VBP_index);
                }
            }
        }

        // In every case of an NN existing, check if its index is higher than VBP, if it is, call it NN3.
        boolean is_NN = isPresent(myArray, "NN");
        int NN_index;
        int NN3_index = 0;
        if(is_NN){
            // Enters here but doesn't pass the next if statement.
            NN_index = locIndex(myArray, "NN");
            System.out.println("Final NNindex is " + NN_index);
            if(NN_index > VBP_index){
                NN3_index = NN_index;
                System.out.println("NN3 exists at: " + NN3_index + "which is after VBP at: " + VBP_index);
            }
        }

        // -------------------------------------------------------------------------------------------------------------
        // Check if the tags exist in the array.
        //boolean is_DT = isPresent(myArray, "DT"); // Beginning with DT
        //boolean is_NN1 = isPresent(myArray, "NN"); // NN after DT
        //boolean is_NN2 = isPresent(myArray, "NN"); // Beginning with NN
        boolean is_NNP = isPresent(myArray, "NNP"); // Beginning with NNP
        //boolean is_VBP = isPresent(myArray, "VBP"); // VBP after any beginning pattern
        //boolean is_NN3 = isPresent(myArray, "NN"); // NN after VBP
        boolean is_JJ = isPresent(myArray, "JJ"); // JJ after VBP
        // Initialize the following variables:
        //int DT_index = 0;
        //int NN1_index = 0;
        //int NN2_index = 0;
        int NNP_index = 0;
        //int VBP_index = 0;
        //int NN3_index = 0;
        int JJ_index = 0;
        // Find and store the index of any tags that exist in the array.
        //if(is_DT){
        //DT_index = locIndex(myArray, "DT");
        //}
        //if(is_NN1){
        //    NN1_index = locIndex(myArray, "NN"); // NN after DT
        //}
        //if(is_NN2){
        //    NN2_index = locIndex(myArray, "NN"); // Beginning with NN
        //}
        if(is_NNP){
            NNP_index = locIndex(myArray, "NNP"); // Beginning with NNP
        }
        //if(is_VBP){
        //    VBP_index = locIndex(myArray, "VBP"); // VBP after any beginning pattern
        //}
        //if(is_NN3){
        //    NN3_index = locIndex(myArray, "NN"); // NN after VBP
        //}
        if(is_JJ){
            JJ_index = locIndex(myArray, "JJ"); // JJ after VBP
        }
        int currentIndex = 0; // Remembers our position in the array.
        int currentState = 0; // Remembers our state in the FSM.
        while(currentState != 6 && currentState != 7) {
            if (DT_index >= currentIndex) {    // By default, this if() statement operates in the zeroth state.
                currentIndex = DT_index;
                //System.out.println("Currently in state: " + currentState);
                //System.out.println("Current Index: " + currentIndex);
                //System.out.println("Found DT at index: " + currentIndex);
                currentState = 1;
                //System.out.println("Sending to: " + currentState);
            } else if (NN1_index >= currentIndex) {
                currentIndex = NN1_index;
                //System.out.println("Currently in state: " + currentState);
                //System.out.println("Current Index: " + currentIndex);
                //System.out.println("Found NN at index: " + currentIndex);
                currentState = 3;
                //System.out.println("Sending to: " + currentState);
            } else if (NNP_index >= currentIndex) {
                currentIndex = NNP_index;
                //System.out.println("Currently in state: " + currentState);
                //System.out.println("Current Index: " + currentIndex);
                //System.out.println("Found NNP at index: " + currentIndex);
                currentState = 4;
                //System.out.println("Sending to: " + currentState);
            } else currentState = 7;
            if (currentState == 1) {
                if (NN2_index >= currentIndex) {
                    currentIndex = NN2_index;
                    //System.out.println("Currently in state: " + currentState);
                    //System.out.println("Current Index: " + currentIndex);
                    //System.out.println("Found NN after DT at index: " + currentIndex);
                    currentState = 2;
                    //System.out.println("Sending to: " + currentState);
                } else currentState = 7;
            }
            if (currentState == 2) {
                if (VBP_index >= currentIndex) {
                    currentIndex = VBP_index;
                    //System.out.println("Currently in state: " + currentState);
                    //System.out.println("Current Index: " + currentIndex);
                    //System.out.println("Found VBP at index: " + currentIndex);
                    currentState = 5;
                    //System.out.println("Sending to: " + currentState);
                } else currentState = 7;
            }
            if (currentState == 3) {
                if (VBP_index >= currentIndex) {
                    currentIndex = VBP_index;
                    //System.out.println("Currently in state: " + currentState);
                    //System.out.println("Current Index: " + currentIndex);
                    //System.out.println("Found VBP at index: " + currentIndex);
                    currentState = 5;
                    //System.out.println("Sending to: " + currentState);
                } else currentState = 7;
            }
            if (currentState == 4) {
                if (VBP_index >= currentIndex) {
                    currentIndex = VBP_index;
                    //System.out.println("Currently in state: " + currentState);
                    //System.out.println("Current Index: " + currentIndex);
                    //System.out.println("Found VBP at index: " + currentIndex);
                    currentState = 5;
                    //System.out.println("Sending to: " + currentState);
                } else currentState = 7;
            }
            if (currentState == 5) {
                //System.out.println("Passed currentState == 5.");
                if (NN3_index >= currentIndex) {
                    //System.out.println("Passed NN3index >= currentIndex.");
                    currentIndex = NN3_index;
                    //System.out.println("Currently in state: " + currentState);
                    //System.out.println("Current Index: " + currentIndex);
                    //System.out.println("Found NN after VBP at index: " + currentIndex);
                    currentState = 6;
                    //System.out.println("Sending to: " + currentState);
                } else if (JJ_index >= currentIndex) {
                    //System.out.println("Passed JJindex >= currentIndex.");
                    currentIndex = JJ_index;
                    //System.out.println("Currently in state: " + currentState);
                    //System.out.println("Current Index: " + currentIndex);
                    //System.out.println("Found JJ after VBP at index: " + currentIndex);
                    currentState = 6;
                    //System.out.println("Sending to: " + currentState);
                } else {
                    currentState = 7;
                    //System.out.println("\nCurrent Index is: " + currentIndex + "\nNN3index is: " + NN3_index + "\nJJindex is: " + JJ_index);
                    //System.out.println("Did Not Pass NN3index or JJindex >= currentIndex, sending to: " + currentState);
                }
            }
        }
        if(currentState == 6){
            System.out.println("Pattern Found!");
            //System.out.println("The words in the sentence that are associated with the POS tags.");
            return "Pattern Found";
        } else{
            // if(currentState == 7) is implied here.
            System.out.println("No Pattern Found.");
            return "No Pattern Found";
        }
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
    public static boolean isPresent(String[] myArray, String pos){
        boolean test = false;
        for (String element : myArray){
            if (Objects.equals(element, pos)){
                test = true;
                break;
            }
        }
        return test;
    }
    public static int locIndex(String[] myArray, String pos){
        if (myArray == null){
            return -1;
        }
        int length = myArray.length;
        int i = 0;
        while (i < length){
            if (Objects.equals(myArray[i], pos)){
                return i;
            }
            else {
                i = i + 1;
            }
        }
        return -1;
    }
}
