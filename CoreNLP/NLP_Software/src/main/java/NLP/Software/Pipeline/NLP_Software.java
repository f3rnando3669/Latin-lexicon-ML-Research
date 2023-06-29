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

            // To-Do:
            //   1. Check the brackets
            //   2. Check the if and else-if statements for congruent logical thought


            String[] myArray = new String[]{"DT", "NN", "VBP", "JJ", ""};


            int DTindex = Arrays.binarySearch(myArray, "DT"); // Beginning with DT
            int NNindex = Arrays.binarySearch(myArray, "NN"); // NN after DT
            int NN2index = Arrays.binarySearch(myArray, "NN"); // Beginning with NN
            int NNPindex = Arrays.binarySearch(myArray, "NNP"); // Beginning with NNP
            int VBPindex = Arrays.binarySearch(myArray, "VBP"); // VBP after any beginning pattern
            int NN3index = Arrays.binarySearch(myArray, "NN"); // NN after VBP
            int JJindex = Arrays.binarySearch(myArray, "JJ"); // JJ after VBP

            int currentIndex = 0; // Remembers our position in the array.
            int currentState = 0; // Remembers our state in the FSM.


            while(currentState != 6 && currentState != 7) {
                if (DTindex >= currentIndex) {    // By default, this if() statement operates in the zeroth state.
                    currentIndex = DTindex;
                    System.out.println("Currently in state: " + currentState);
                    System.out.println("Current Index: " + currentIndex);
                    System.out.println("Found DT at index: " + currentIndex);
                    currentState = 1;
                    System.out.println("Sending to: " + currentState);
                } else if (NNindex >= currentIndex) {
                    currentIndex = NNindex;
                    System.out.println("Currently in state: " + currentState);
                    System.out.println("Current Index: " + currentIndex);
                    System.out.println("Found NN at index: " + currentIndex);
                    currentState = 3;
                    System.out.println("Sending to: " + currentState);
                } else if (NNPindex >= currentIndex) {
                    currentIndex = NNPindex;
                    System.out.println("Currently in state: " + currentState);
                    System.out.println("Current Index: " + currentIndex);
                    System.out.println("Found NNP at index: " + currentIndex);
                    currentState = 4;
                    System.out.println("Sending to: " + currentState);
                } else currentState = 7;


                 if(currentState == 1){
                     if(NN2index >= currentIndex){
                         currentIndex = NN2index;
                         System.out.println("Currently in state: " + currentState);
                         System.out.println("Current Index: " + currentIndex);
                         System.out.println("Found NN after DT at index: " + currentIndex);
                         currentState = 2;
                         System.out.println("Sending to: " + currentState);
                     } else currentState = 7;
                 }

                 if(currentState == 2){
                     if(VBPindex >= currentIndex){
                         currentIndex = VBPindex;
                         System.out.println("Currently in state: " + currentState);
                         System.out.println("Current Index: " + currentIndex);
                         System.out.println("Found VBP at index: " + currentIndex);
                         currentState = 5;
                         System.out.println("Sending to: " + currentState);
                     } else currentState = 7;
                 }

                 if(currentState == 3){
                     if(VBPindex >= currentIndex){
                         currentIndex = VBPindex;
                         System.out.println("Currently in state: " + currentState);
                         System.out.println("Current Index: " + currentIndex);
                         System.out.println("Found VBP at index: " + currentIndex);
                         currentState = 5;
                         System.out.println("Sending to: " + currentState);
                     } else currentState = 7;
                    }

                 if(currentState == 4){
                     if(VBPindex >= currentIndex){
                         currentIndex = VBPindex;
                         System.out.println("Currently in state: " + currentState);
                         System.out.println("Current Index: " + currentIndex);
                         System.out.println("Found VBP at index: " + currentIndex);
                         currentState = 5;
                         System.out.println("Sending to: " + currentState);
                     } else currentState = 7;
                 }

                 if(currentState == 5) {
                     System.out.println("Passed currentState == 5.");
                     if (NN3index >= currentIndex) {
                         System.out.println("Passed NN3index >= currentIndex.");
                         currentIndex = NN3index;
                         System.out.println("Currently in state: " + currentState);
                         System.out.println("Current Index: " + currentIndex);
                         System.out.println("Found NN after VBP at index: " + currentIndex);
                         currentState = 6;
                         System.out.println("Sending to: " + currentState);
                     } else if (JJindex >= currentIndex) {
                         System.out.println("Passed JJindex >= currentIndex.");
                         currentIndex = JJindex;
                         System.out.println("Currently in state: " + currentState);
                         System.out.println("Current Index: " + currentIndex);
                         System.out.println("Found JJ after VBP at index: " + currentIndex);
                         currentState = 6;
                         System.out.println("Sending to: " + currentState);
                     } else {
                         currentState = 7;
                         System.out.println("\nCurrent Index is: " + currentIndex + "\nNN3index is: " + NN3index + "\nJJindex is: " + JJindex);
                         System.out.println("Did Not Pass NN3index or JJindex >= currentIndex, sending to: " + currentState);
                     }
                 }
            }

            if(currentState == 6){
                System.out.println("Pattern Match!");
                //System.out.println("The words in the sentence that are associated with the POS tags.");
                return "Pattern Found";
            } else{
                // if(currentState == 7) is implied here.
                System.out.println("No Pattern Found.");
                return "No Pattern Found";
               }
        }
    }
