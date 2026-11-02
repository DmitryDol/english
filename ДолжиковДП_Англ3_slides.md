# Self-RAG: Slide Plan for the Oral Presentation

**Speaker:** Dmitry Dolzhikov  
**Slides:** 13  
**Speech:** 764 words, about 6 minutes at 130 words per minute (the speech is TASK 3 of `ДолжиковДП_Англ3.md`, split by slides without changes)

## Instructions for the presentation generator

1. Create a 16:9 presentation in English with exactly 13 slides, in the order given below.
2. Use the slide title and the "On-slide text" as the visible content. Keep the text short. Do not add facts, numbers or claims that are not in this document.
3. Copy the "Speaker notes" of each slide into the notes of that slide exactly as written.
4. Where an image is named, insert the attached file with that name on that slide, together with its caption in small font. Do not redraw, crop or recolour the figures. Where no image is named, do not invent charts or data; a table built from the on-slide text, a simple layout or a neutral icon is enough.
5. Style: clean academic design, light background, one accent colour, a sans-serif font, large readable text, no more than one image per slide.

Image files to attach (from `articles/article3_figures/` in the repository): `figure1_left_RAG.png`, `figure1_right_SelfRAG.png`, `figure2.png`, `figure3_panels_BC.png`.

## Slide 1. Self-RAG: A Language Model That Retrieves, Generates and Criticises Its Own Answers

**Time:** about 29 seconds (63 words)

**On-slide text:**

- Dmitry Dolzhikov
- Based on: A. Asai, Z. Wu, Y. Wang, A. Sil, H. Hajishirzi. "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection". ICLR 2024
- University of Washington, Allen Institute for AI, IBM Research AI

**Image:** none.

**Layout:** Title slide.

**Speaker notes:**

> Good afternoon, ladies and gentlemen. Thank you all for coming today. My name is Dmitry Dolzhikov. Today I am going to talk about the article "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection". It was written by researchers from the University of Washington, the Allen Institute for AI and IBM Research, and presented at ICLR 2024, a major conference on machine learning.

## Slide 2. The Problem with Standard RAG

**Time:** about 25 seconds (55 words)

**On-slide text:**

- LLMs write fluent answers but make factual mistakes
- RAG: find documents and add them to the model input
- Standard RAG always retrieves K documents, even when they are not needed
- It never checks whether the answer agrees with the documents

**Image:** `figure1_left_RAG.png` (`articles/article3_figures/figure1_left_RAG.png`). Caption: "Conventional RAG: always retrieves K documents and generates without checking them. Source: Asai et al., ICLR 2024, Figure 1 (left)."

**Layout:** Image on the left (tall), bullets on the right.

**Speaker notes:**

> Large language models write fluent answers, but they often make factual mistakes. A common fix is retrieval-augmented generation, or RAG: the system finds documents and adds them to the model's input. Standard RAG, however, searches every time, even when it is not needed, and it never checks whether the answer actually agrees with the documents.

## Slide 3. Outline

**Time:** about 18 seconds (38 words)

**On-slide text:**

- The main idea of Self-RAG
- Training the model
- Experiments and results
- What this means for reliable language models

**Image:** none.

**Layout:** Numbered list.

**Speaker notes:**

> To start with, I'll describe the main idea of Self-RAG. Then I'll mention how the authors train the model. Next, I'll discuss the experiments and the results. Finally, I'll summarize what this means for building reliable language models.

## Slide 4. Reflection Tokens

**Time:** about 38 seconds (83 words)

**On-slide text:**

- One model: retrieve when needed, generate, criticise its own output
- Retrieve {yes, no, continue}: should the model search?
- IsRel {relevant, irrelevant}: is the passage relevant?
- IsSup {fully supported, partially supported, no support}: is the output supported by the passage?
- IsUse {5, 4, 3, 2, 1}: how useful is the whole response?

**Image:** none.

**Layout:** The first line as a subtitle, then a four-row table built from the other lines (token name, values, question), based on Table 1 of the article. Show the token names in a monospace font. No other content.

**Speaker notes:**

> Let's begin by looking at the main idea. Self-RAG teaches one language model to do three things: to retrieve when it needs to, to generate an answer, and to criticise its own answer. It does this with special words called reflection tokens. There are four types. Retrieve says whether the model should search. IsRel says whether a found passage is relevant. IsSup says whether the answer is supported by the passage. IsUse rates how useful the whole answer is, from one to five.

## Slide 5. Self-RAG at Work

**Time:** about 30 seconds (65 words)

**On-slide text:**

- "How did US states get their names?": Retrieve, then 3 passages
- A continuation for each passage, generated in parallel
- Critique tokens select the relevant and fully supported segment
- "Write an essay of your best summer vacation": no retrieval

**Image:** `figure1_right_SelfRAG.png` (`articles/article3_figures/figure1_right_SelfRAG.png`). Caption: "Self-RAG retrieves on demand, generates segments in parallel and selects the best one. Source: Asai et al., ICLR 2024, Figure 1 (right)."

**Layout:** Large image across most of the slide, short bullets below or beside it.

**Speaker notes:**

> Where does that lead us? The model can now look at its own work. When it is asked how US states got their names, it retrieves several passages, writes a continuation for each of them in parallel, and keeps the one that is relevant and fully supported. When it is asked to write an essay about a summer vacation, it does not search at all.

## Slide 6. Training: Critic and Generator

**Time:** about 53 seconds (114 words)

**On-slide text:**

- GPT-4 labels: 4k–20k examples for each token type
- Critic model trained on these labels: over 90% agreement with GPT-4 for most token types
- The critic inserts reflection tokens into 150k training examples
- Generator (Llama 2, 7B or 13B) learns text and tokens together; no critic at test time

**Image:** `figure2.png` (`articles/article3_figures/figure2.png`). Caption: "Self-RAG training examples: without retrieval (left) and with retrieved passages (right). Source: Asai et al., ICLR 2024, Figure 2."

**Layout:** Image on the right, the four steps as a short vertical flow on the left.

**Speaker notes:**

> Well, I've told you about the idea. Now we'll move on to the training. Labelling every sentence by hand would be very expensive, so the authors asked GPT-4 to produce reflection tokens for a sample of examples, between four and twenty thousand for each type. They trained their own critic model on these labels, and it agreed with GPT-4 in more than ninety percent of cases for most token types. The critic then added reflection tokens to one hundred and fifty thousand training examples. Finally, the main model, Llama 2 with seven or thirteen billion parameters, learned to generate the text and the tokens together, so the critic is not needed at test time.

## Slide 7. Control at Test Time

**Time:** about 18 seconds (40 words)

**On-slide text:**

- The model writes the reflection tokens itself
- Weights: e.g. a higher weight on IsSup means more focus on support
- Threshold: retrieve more or less often
- No retraining needed

**Image:** none.

**Layout:** Two blocks side by side ("Weights" and "Threshold"), each with a simple neutral slider icon; no charts or numbers.

**Speaker notes:**

> Let's consider this in more detail. Because the model writes these tokens itself, users can control it without retraining. A weight can make the model care more about support, and a threshold can make it search more or less often.

## Slide 8. Six Evaluation Tasks

**Time:** about 12 seconds (27 words)

**On-slide text:**

- Short-form QA: PopQA, TriviaQA
- Closed-set: PubHealth (fact checking), ARC-Challenge (reasoning)
- Long-form: biography generation, ASQA (answers with citations)

**Image:** none.

**Layout:** Three columns or three cards, one per task group.

**Speaker notes:**

> Let me turn now to the results. The authors tested Self-RAG on six tasks, from short questions and fact checking to biographies and long answers with citations.

## Slide 9. Main Results: Self-RAG 13B vs ChatGPT

**Time:** about 34 seconds (74 words)

**On-slide text:**

- PopQA (rare entities), accuracy: Self-RAG 55.8 vs ChatGPT 29.3
- PubHealth (health fact checking), accuracy: Self-RAG 74.5 vs ChatGPT 70.1
- ASQA citation precision: Self-RAG 70.3 vs ChatGPT with retrieval 65.1

**Image:** none.

**Layout:** Comparison table with three rows (task, Self-RAG 13B, ChatGPT) built from these numbers only (Table 2 of the article); highlight the Self-RAG column. Add the note "Source: Asai et al., ICLR 2024, Table 2" in small font.

**Speaker notes:**

> What does this mean for accuracy? To give you an example, on PopQA, a dataset of questions about rare entities, the thirteen-billion-parameter model reached about fifty-six percent accuracy, while ChatGPT without retrieval reached twenty-nine percent. On PubHealth, a health fact-checking task, Self-RAG scored seventy-four point five and ChatGPT seventy point one. For long answers with citations, the citation precision of Self-RAG was about seventy percent, higher than the sixty-five percent of ChatGPT with retrieval.

## Slide 10. Why Reflection Tokens Matter

**Time:** about 29 seconds (63 words)

**On-slide text:**

- Llama2-FT 7B: same training data, no reflection tokens
- PopQA accuracy: Llama2-FT 7B 48.7 vs Self-RAG 7B 54.9
- The gain comes from the method, not only from the data

**Image:** none.

**Layout:** Two large numbers side by side (48.7 and 54.9) with their model names, the last line below them. Add the note "Source: Asai et al., ICLR 2024, Table 2" in small font.

**Speaker notes:**

> A good example of this is a simple comparison that shows the value of reflection tokens. The authors also trained Llama 2 on the same data, but without the tokens. This model was clearly weaker: on PopQA it reached about forty-nine percent, against fifty-five for Self-RAG of the same size. So the gain comes from the method and not only from the data.

## Slide 11. Trade-offs

**Time:** about 14 seconds (30 words)

**On-slide text:**

- Higher IsSup weight: higher citation precision, lower fluency (MAUVE) on ASQA
- Higher retrieval threshold: fewer searches; accuracy drops on PopQA more than on PubHealth

**Image:** `figure3_panels_BC.png` (`articles/article3_figures/figure3_panels_BC.png`). Caption: "Effect of the IsSup weight on ASQA (b) and of the retrieval threshold on PubHealth and PopQA (c). Source: Asai et al., ICLR 2024, Figure 3 (b, c)."

**Layout:** Wide image across the slide, two bullets under it.

**Speaker notes:**

> The authors also show the trade-offs. A higher weight for support gives more precise citations but less fluent text, and searching less often saves time but costs accuracy on PopQA.

## Slide 12. Conclusions

**Time:** about 31 seconds (68 words)

**On-slide text:**

- One model decides when to search and checks its own answers with reflection tokens
- Open 7B and 13B models outperform ChatGPT on several tasks and give more precise citations
- Behaviour can be tuned at test time; claims are still not always fully supported

**Image:** none.

**Layout:** Three numbered points.

**Speaker notes:**

> In conclusion, let me sum up the main findings. First, Self-RAG lets one model decide when to search and check its own answers with reflection tokens. Second, open models with seven and thirteen billion parameters outperform ChatGPT on several tasks and give more precise citations. Third, their behaviour can be tuned at test time, although the model can still make claims that its sources do not fully support.

## Slide 13. Key Message

**Time:** about 20 seconds (44 words)

**On-slide text:**

- A language model becomes more reliable when it learns to check its own answers against its sources
- Thank you! Questions?

**Image:** none.

**Layout:** Large quote in the centre, "Thank you! Questions?" below it.

**Speaker notes:**

> If you take just one thing from this talk, take this: a language model becomes more reliable when it learns to check its own answers against its sources. Many thanks for your attention. Now I'll be glad to answer any questions you may have.
