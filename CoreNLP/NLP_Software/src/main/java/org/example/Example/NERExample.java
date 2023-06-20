package org.example.Example;

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;

import java.util.List;

public class NERExample {

    public static void main(String[] args) {

        StanfordCoreNLP stanfordCoreNLP = Pipeline.getPipeline();

        //String text = "Hey! My name is Sanskriti Baranwal and I have friend his name Anthony." + " We both are living in Texas";

        String text2 = "The ISIS has claimed responsibility for a suicide bomb blast in the Tunisian capital earlier this week, the militant group's Amaq news agency said on Thursday. A militant wearing an explosives belt blew himself up in Tunis.";

        CoreDocument coreDocument = new CoreDocument(text2);

        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabels = coreDocument.tokens();

        for (CoreLabel coreLabel : coreLabels) {

            String ner = coreLabel.get(CoreAnnotations.NamedEntityTagAnnotation.class);

            System.out.println(coreLabel.originalText() + " = " + ner);
        }
    }
}
