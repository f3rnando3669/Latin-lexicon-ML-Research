package NLP_Pipeline;

import com.robbinstony.nlp.Pipeline;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.CoreSentence;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
//import edu.stanford.nlp.naturalli.VerbTense;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;

public class NLP_Pipeline {
    public static StanfordCoreNLP stanfordCoreNLP = Pipeline.getPipeline();

    public static void main(String[] args) throws FileNotFoundException {

        Scanner scanner = new Scanner(new File("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//input.txt"));

        PrintWriter out = new PrintWriter("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//output.txt");

        while(scanner.hasNextLine()){
            String input = scanner.nextLine();
            //System.out.println("Input: " + input);

            String lemmaOutput = Lemma(input);
            //System.out.println("Post-Lemma: " + lemmaOutput);

            String POSoutput = POS(lemmaOutput);
            //System.out.println("Post-POS: " + POSoutput);

            String SRoutput = SentenceRecognizer(POSoutput);
            //System.out.println(SRoutput)    ;

            String PatternMatchedOutput = PatternMatching(SRoutput);
            //System.out.println("Post-PatternMatching: " + PatternMatchedOutput);

            out.println("Input: " + input + "\nPost-Lemma: " + lemmaOutput + "\nPost-POS: " + POSoutput + "\nPatternMatching: " + PatternMatchedOutput + "\nFinal Output: " + SRoutput);
        }
        scanner.close();
        out.close();
    }

    public static String SentenceRecognizer(String input){
        CoreDocument coreDocument = new CoreDocument(input);

        stanfordCoreNLP.annotate(coreDocument);

        List<CoreSentence> sentences = coreDocument.sentences();

        StringBuilder output = new StringBuilder();
        for (CoreSentence sentence : sentences){
            output.append(sentence.toString()).append("\n");
        }
        return output.toString();
    }

    public static String Lemma(String SRoutput){
        CoreDocument coreDocument = new CoreDocument(SRoutput);
        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();
        String[] words = new String[coreLabelList.size()];

        int i = 0;

        for(CoreLabel coreLabel : coreLabelList){
            words[i] = coreLabel.lemma();
            i++;
        }

        String output = String.join(" ", words);

        return output;
    }

    public static String POS(String Lemmaoutput){
        CoreDocument coreDocument = new CoreDocument(Lemmaoutput);
        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();
        String[] words = new String[coreLabelList.size()];

        int i = 0;

        for(CoreLabel coreLabel : coreLabelList){
            words[i] = coreLabel.get(CoreAnnotations.PartOfSpeechAnnotation.class);
            i++;
        }

        String output = String.join(" ", words);

        return output;
    }

    public static String PatternMatching(String POSoutput) {

        // To-Do:
        //   1. Make is_NN2,3 and NN2,3_index smarter to they actually differentiate the NNs, if possible.
        //   2. Store each instance of NN, and then continue the search from the index of the first NN.
        //   3. Only look for different NNs if certain conditions have passed.
        //        - Ex.  IF is_DT is true, then search for is_NN1, otherwise search for is_NN2.
        //               Always search for is_NN3, but two different ways for following NN1 vs NN2.

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

    public static boolean isPresent(String myArray[], String pos){
        boolean test = false;

        for (String element : myArray){
            if (element == pos){
                test = true;
                break;
            }
        }
        return test;
    }

    public static int locIndex(String myArray[], String pos){
        if (myArray == null){
            return -1;
        }

        int length = myArray.length;
        int i = 0;

        while (i < length){
            if (myArray[i] == pos){
                return i;
            }
            else {
                i = i + 1;
            }
        }
        return -1;
    }
}
