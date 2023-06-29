package NLP_Pipeline;

import com.robbinstony.nlp.Pipeline;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.CoreSentence;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.simple.Sentence;
import edu.stanford.nlp.trees.tregex.tsurgeon.JJTTsurgeonParserState;
//import edu.stanford.nlp.naturalli.VerbTense;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.lang.reflect.Array;
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

    public static String PatternMatching(String POSoutput){

        String[] myArray = new String[]{"NN", "VBP", "JJ"};

        int DTindex = Arrays.binarySearch(myArray, "DT");
        int NNindex = Arrays.binarySearch(myArray, "NN");
        int NN2index = Arrays.binarySearch(myArray, "NN");
        int NNPindex = Arrays.binarySearch(myArray, "NNP");
        int VBPindex = Arrays.binarySearch(myArray, "VBP");
        int NN3index = Arrays.binarySearch(myArray, "NN");
        int JJindex = Arrays.binarySearch(myArray, "JJ");

        int currentIndex = 0;
        int currentState = 0;


        while(currentState != 7 && currentState !=8){
             // This if is in currentState == 0 already.
             if (DTindex >= currentIndex) {
                 System.out.println("Found DT at " + currentIndex);
                 currentIndex = DTindex + 1;
                 currentState = 1;
             } else if (NNindex >= currentIndex) {
                 System.out.println("Found NN at " + currentIndex);
                 currentIndex = NNindex + 1;
                 currentState = 3;
             } else if (NNPindex >= currentIndex) {
                 System.out.println("Found NNP at " + currentIndex);
                 currentIndex = NNPindex + 1;
                 currentState = 4;
             } else currentState = 8;

             if(currentState == 1){
                 if(NN2index >= currentIndex){
                     System.out.println("Found NN after DT at " + currentIndex);
                     currentIndex = NN2index + 1;
                     currentState = 2;
                 } else currentState = 8;
             }

             if(currentState == 2){
                 if(VBPindex >= currentIndex){
                     System.out.println("Found VBP at " + currentIndex);
                     currentIndex = VBPindex + 1;
                     currentState = 5;
                 } else currentState = 8;
             }

             if(currentState == 3){
                 if(VBPindex >= currentIndex){
                     System.out.println("Found VBP at " + currentIndex);
                     currentIndex = VBPindex + 1;
                     currentState = 5;
                 } else currentState = 8;
                }

             if(currentState == 4){
                 if(VBPindex >= currentIndex){
                     System.out.println("Found VBP at " + currentIndex);
                     currentIndex = VBPindex + 1;
                     currentState = 5;
                 } else currentState = 8;
             }

             if(currentState == 5){
                 if(NN3index >= currentIndex){
                     System.out.println("Found NN after VBP at " + currentIndex);
                     currentIndex = NN3index + 1;
                     currentState = 6;
                 } else currentState = 8;
             }

             if(currentState == 6){
                 if(JJindex >= currentIndex){
                     System.out.println("Found JJ after VBP at " + currentIndex);
                     currentIndex = JJindex + 1;
                     currentState = 7;
                 } else currentState = 8;
             }
        }

        if(currentState == 7){
            System.out.println("Pattern Match!");
            //System.out.println("The words in the sentence that are associated with the POS tags.");
            return "Pattern Found";
        } else{
            // if(currentState == 8) is implied here.
            System.out.println("No Pattern Found.");
            return "No Pattern Found";
           }
    }

    public static int countSentences(String input){
        if(input == null || input.isEmpty()){
            return 0;
        }

        String[] sentences = input.split("[.]+");

        return sentences.length;
    }
}
