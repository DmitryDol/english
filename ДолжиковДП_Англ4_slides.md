# CRAG: Slide Plan for the Oral Presentation

**Speaker:** Dmitry Dolzhikov  
**Slides:** 14  
**Speech:** 818 words, about 6 minutes at 130 words per minute (the speech is TASK 3 of `ДолжиковДП_Англ4.md`, split by slides without changes)

## Instructions for the presentation generator

1. Create a 16:9 presentation in English with exactly 14 slides, in the order given below.
2. Use the slide title and the "On-slide text" as the visible content. Keep the text short. Do not add facts, numbers or claims that are not in this document.
3. Copy the "Speaker notes" of each slide into the notes of that slide exactly as written.
4. Where an image is named, insert the attached file with that name on that slide, together with its caption in small font. Do not redraw, crop or recolour the figures. Where no image is named, do not invent charts or data; a table built from the on-slide text, a simple layout or a neutral icon is enough.
5. Style: clean academic design, light background, one accent colour, a sans-serif font, large readable text, no more than one image per slide.

Image files to attach (from `articles/article4_figures/` in the repository): `figure1.png`, `figure2.png`, `figure2_refine_search.png`, `figure3_chart.png`.

## Slide 1. CRAG: Checking and Correcting Retrieved Documents in Retrieval-Augmented Generation

**Time:** about 30 seconds (65 words)

**On-slide text:**

- Dmitry Dolzhikov
- Based on: S.-Q. Yan, J.-C. Gu, Y. Zhu, Z.-H. Ling. "Corrective Retrieval Augmented Generation". arXiv:2401.15884v3, 2024
- University of Science and Technology of China, University of California, Los Angeles, Google DeepMind

**Image:** none.

**Layout:** Title slide.

**Speaker notes:**

> Good afternoon, ladies and gentlemen. Thank you all for coming today. My name is Dmitry Dolzhikov. Today I am going to talk about the article "Corrective Retrieval Augmented Generation", or CRAG for short. It was written by researchers from the University of Science and Technology of China, the University of California, Los Angeles, and Google DeepMind, and published as a preprint on arXiv in 2024.

## Slide 2. Hallucinations and Retrieval

**Time:** about 24 seconds (51 words)

**On-slide text:**

- LLMs hallucinate: fluent answers with wrong facts
- RAG: find documents and give them to the model with the question
- What if the retriever finds the wrong documents?
- Most RAG systems simply trust them

**Image:** none.

**Layout:** Text slide; a simple neutral icon is allowed, no charts.

**Speaker notes:**

> Large language models often hallucinate: they write fluent answers that contain wrong facts. A common fix is retrieval-augmented generation, or RAG. The system finds documents and gives them to the model together with the question. But what happens if the retriever finds the wrong documents? Most RAG systems simply trust them.

## Slide 3. Outline

**Time:** about 19 seconds (42 words)

**On-slide text:**

- The problem of poor retrieval
- How CRAG checks and corrects retrieved documents
- Experiments and results
- What this means for reliable question answering

**Image:** none.

**Layout:** Numbered list.

**Speaker notes:**

> To start with, I'll describe the problem of poor retrieval. Then I'll mention how CRAG checks and corrects the retrieved documents. Next, I'll discuss the experiments and the results. Finally, I'll summarize what this work means for building reliable question answering systems.

## Slide 4. When Retrieval Goes Wrong

**Time:** about 30 seconds (66 words)

**On-slide text:**

- Question: "Who was the screenwriter for Death of a Batman?"
- Retrieved document: about the 1989 film "Batman"
- Answer: "Hamm" (wrong)
- A weak retriever can mislead the generator

**Image:** `figure1.png` (`articles/article4_figures/figure1.png`). Caption: "Accurate and inaccurate retrieved documents and the answers of the generator. Source: Yan et al., arXiv:2401.15884v3 (2024), Figure 1."

**Layout:** Image on the right (tall), bullets on the left.

**Speaker notes:**

> Let's begin by looking at the problem. The authors show a simple example. The question is: "Who was the screenwriter for Death of a Batman?" The retriever returns a document about the 1989 film Batman, which mentions a script by someone called Hamm. The model trusts this document and answers "Hamm", which is wrong. So a weak retriever can mislead the model instead of helping it.

## Slide 5. The Retrieval Evaluator

**Time:** about 42 seconds (90 words)

**On-slide text:**

- Fine-tuned T5-large: 0.77B parameters
- Scores every retrieved document (about 10 per question)
- Correct: at least one document above the upper threshold
- Incorrect: all documents below the lower threshold
- Ambiguous: all other cases

**Image:** `figure2.png` (`articles/article4_figures/figure2.png`). Caption: "Overview of CRAG at inference: retrieval, knowledge correction and generation. Source: Yan et al., arXiv:2401.15884v3 (2024), Figure 2."

**Layout:** Large image across most of the slide, short bullets beside or below it.

**Speaker notes:**

> Where does that lead us? The authors add a small component between the retriever and the generator, called the retrieval evaluator. It is based on the T5-large model and has only about seven hundred and seventy million parameters. The evaluator gives a relevance score to every retrieved document, and then one of three actions is triggered. If at least one document scores above an upper threshold, the action is Correct. If all documents score below a lower threshold, the action is Incorrect. In all other cases the action is Ambiguous.

## Slide 6. Three Actions

**Time:** about 47 seconds (101 words)

**On-slide text:**

- Correct: split into knowledge strips, filter, recompose (internal knowledge)
- Incorrect: discard the documents, rewrite the query with ChatGPT, search the web, prefer Wikipedia (external knowledge)
- Ambiguous: combine internal and external knowledge
- Plug-and-play: only the input of the generator changes

**Image:** `figure2_refine_search.png` (`articles/article4_figures/figure2_refine_search.png`). Caption: "Knowledge refinement (top) and knowledge searching (bottom) in CRAG. Source: Yan et al., arXiv:2401.15884v3 (2024), Figure 2 (detail)."

**Layout:** Image on the left, bullets on the right.

**Speaker notes:**

> Well, I've told you about the evaluator. Now we'll move on to the three actions. For Correct, the system refines the documents. It splits them into small knowledge strips of one or a few sentences, scores each strip, removes the irrelevant ones and joins the rest. For Incorrect, the retrieved documents are thrown away. ChatGPT rewrites the question as a short keyword query, and the system searches the web, preferring Wikipedia pages. For Ambiguous, both kinds of knowledge are combined. Because CRAG only changes what the generator receives, it can be added to an existing system. The authors call it plug-and-play.

## Slide 7. Experimental Setup

**Time:** about 24 seconds (53 words)

**On-slide text:**

- CRAG = standard RAG + corrective strategies; Self-CRAG = Self-RAG + corrective strategies
- PopQA: short questions about rare entities (accuracy)
- Biography: long texts about people (FactScore)
- PubHealth: true-or-false health claims (accuracy)
- ARC-Challenge: multiple-choice science questions (accuracy)

**Image:** none.

**Layout:** The first line as a subtitle, then a four-row table of datasets (dataset, task, metric) built from the other lines.

**Speaker notes:**

> Let's consider this in more detail. The authors combined their method with standard RAG, which gives CRAG, and with Self-RAG, which gives Self-CRAG. They tested both on four datasets: PopQA with short questions about rare entities, Biography with long texts about people, PubHealth with true-or-false health claims, and ARC-Challenge with multiple-choice science questions.

## Slide 8. Main Results

**Time:** about 30 seconds (65 words)

**On-slide text:**

- Generator: SelfRAG-LLaMA2-7b
- PopQA accuracy: RAG 52.8 → CRAG 59.8
- PubHealth accuracy: RAG 39.0 → CRAG 75.6
- Biography FactScore: Self-RAG 81.2 → Self-CRAG 86.2

**Image:** none.

**Layout:** Comparison table with three rows (task, baseline, CRAG or Self-CRAG) built from these numbers only (Table 1 of the article); highlight the CRAG column. Add the note "Source: Yan et al., 2024, Table 1" in small font.

**Speaker notes:**

> Let me turn now to the results. What does this mean for accuracy? To give you an example, with the Self-RAG version of Llama 2 as the generator, CRAG raised the accuracy of standard RAG on PopQA from about fifty-three to almost sixty percent, and on PubHealth from thirty-nine to about seventy-six percent. Self-CRAG reached a FactScore of eighty-six on biographies, while Self-RAG reached eighty-one.

## Slide 9. The Evaluator vs ChatGPT

**Time:** about 20 seconds (44 words)

**On-slide text:**

- Accuracy of judging retrieval results on PopQA:
- T5-based evaluator: 84.3
- ChatGPT: 58.0
- ChatGPT with Chain-of-Thought: 62.4
- ChatGPT few-shot: 64.7

**Image:** none.

**Layout:** Table with four rows built from these numbers only (Table 4 of the article); highlight the T5-based evaluator. Add the note "Source: Yan et al., 2024, Table 4" in small font.

**Speaker notes:**

> A good example of this is the evaluator itself. On PopQA it judged the retrieved documents correctly in about eighty-four percent of cases, while ChatGPT managed only fifty-eight percent. So a small specialised model can do this job better than a large general one.

## Slide 10. Works with an Ordinary Generator

**Time:** about 18 seconds (38 words)

**On-slide text:**

- PopQA accuracy:
- Self-RAG with its own fine-tuned model: 54.9
- Self-RAG with the original LLaMA2-hf-7b: 29.0
- CRAG with the original LLaMA2-hf-7b: 54.9

**Image:** none.

**Layout:** Three large numbers side by side with their labels (Table 1 of the article). Add the note "Source: Yan et al., 2024, Table 1" in small font.

**Speaker notes:**

> The method also works with an ordinary generator. When the special Self-RAG model was replaced with the original Llama 2, the accuracy of Self-RAG on PopQA fell from fifty-five to twenty-nine percent, while CRAG still reached fifty-five percent.

## Slide 11. Where Does the Gain Come From?

**Time:** about 19 seconds (41 words)

**On-slide text:**

- Same web search results for the baselines: small gain (PopQA, SelfRAG-LLaMA2-7b: RAG with web search 53.8, CRAG 59.8)
- Removing any action or knowledge step (refinement, query rewriting, selection) lowers accuracy
- Example: Self-CRAG with LLaMA2-hf-7b without knowledge selection: 49.0 → 24.9 on PopQA

**Image:** none.

**Layout:** Three short blocks; numbers from Tables 3 and 5 of the article only, no charts.

**Speaker notes:**

> The authors also checked where the gain comes from. When they simply gave standard RAG and Self-RAG the same web search results, the improvement was small. Removing any of the three actions, or any step of knowledge processing, lowered the accuracy.

## Slide 12. Robustness and Cost

**Time:** about 19 seconds (42 words)

**On-slide text:**

- Retrieval accuracy lowered from 69.8 to 10: Self-CRAG drops less than Self-RAG
- Generation time per question: RAG 0.363 s, CRAG 0.512 s
- TFLOPs per token: RAG 26.5, CRAG 27.2

**Image:** `figure3_chart.png` (`articles/article4_figures/figure3_chart.png`). Caption: "Generation accuracy of Self-RAG and Self-CRAG on PopQA as retrieval accuracy decreases. Source: Yan et al., arXiv:2401.15884v3 (2024), Figure 3."

**Layout:** Large chart, three short lines under it.

**Speaker notes:**

> When they made retrieval worse on purpose, Self-CRAG lost much less accuracy than Self-RAG. The extra cost is modest: the generation step took about zero point five seconds per question with CRAG, compared with zero point three six seconds for standard RAG.

## Slide 13. Conclusions

**Time:** about 33 seconds (72 words)

**On-slide text:**

- A lightweight evaluator checks retrieved documents and chooses: refine, search the web, or both
- Better results for standard RAG and Self-RAG on short-form, long-form and closed-set tasks, with different generators
- Limitation: a separately fine-tuned evaluator is still needed

**Image:** none.

**Layout:** Three numbered points.

**Speaker notes:**

> In conclusion, let me sum up the main findings. First, CRAG checks the retrieved documents with a lightweight evaluator and chooses one of three actions: refine the documents, search the web, or do both. Second, it improves standard RAG and Self-RAG on short-form, long-form and closed-set tasks, and it works with different generators. Third, it still needs a separately fine-tuned evaluator, and the authors plan to remove this dependence in future work.

## Slide 14. Key Message

**Time:** about 22 seconds (48 words)

**On-slide text:**

- A system that checks its sources before it answers is more reliable than a system that trusts every document it finds
- Thank you! Questions?

**Image:** none.

**Layout:** Large quote in the centre, "Thank you! Questions?" below it.

**Speaker notes:**

> If you take just one thing from this talk, take this: a system that checks its sources before it answers is more reliable than a system that trusts every document it finds. Many thanks for your attention. Now I'll be glad to answer any questions you may have.
