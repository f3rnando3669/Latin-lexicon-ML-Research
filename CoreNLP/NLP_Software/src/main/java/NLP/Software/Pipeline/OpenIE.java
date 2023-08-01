package NLP.Software.Pipeline;
import edu.stanford.nlp.ie.util.RelationTriple;
import edu.stanford.nlp.simple.*;

import java.io.File;
import java.io.PrintWriter;
import java.util.Scanner;

public class OpenIE {
    public static void main(String[] args) throws Exception {

        Scanner scanner = new Scanner(new File("C:/Users/sansk/IdeaProjects/NLP_Software/src/main/java/NLP/Software/Pipeline/input.txt"));

        PrintWriter out = new PrintWriter("C:/Users/sansk/IdeaProjects/NLP_Software/src/main/java/NLP/Software/Pipeline/OpenIEoutput.txt");

        while (scanner.hasNextLine()) {
            // Reads each line of input
            String input = scanner.nextLine();

            // Create a CoreNLP document
            Document doc = new Document(input);

            // Iterate over the sentences in the document
            for (Sentence sent : doc.sentences()) {
                // Iterate over the triples in the sentence
                for (RelationTriple triple : sent.openieTriples()) {
                    // Print the triple
                    out.println(triple.subjectLemmaGloss() + " " + triple.relationLemmaGloss() + " " + triple.objectLemmaGloss());
                }
            }
        }
        scanner.close();
        out.close();
    }
}
