# Why Storing AI Outputs Matters!

08-Jan-25

*Note: this is less of a specific "idea" as it is a manifesto outlining why I've been engaged by this idea and how I envision it fitting into much broader projects! This text was captured using the excellent [Voice Notes](https://voicenotes.com) and has been edited lightly for clarity*

## "But where do the outputs go?"

My first strong feeling about large language models after I began using them seriously in early 2024 was that output storage is the key neglected element of the first crop of mainstream large language model tools on the market. 

During parts of 2024, I worked on some systems for creating CRUD apps for ensuring that outputs were stored in an organized relational database. 

These prototypes were not terribly exciting and were built for my own use but they were functional. 

My idea in developing them was less to develop new shiny AI tools and more to test out the utility that might be derived from doing this in the first place. 

Perhaps because I am something of a data hoarder (okay, I'm very much a data hoarder) one of the first thoughts that came to my mind when beginning to leverage these tools for work and in personal use was "some of this information is great what are you supposed to do about storing it?" It is curious that output storage hasn't received more love and attention from vendors to date.

## If we store prompts, we should store outputs

Prompt engineering has been recognized as a very important discipline in AI.

Although it's been forecast that more advanced models will ultimately make good knowledge of prompt engineering redundant, so far we have not seen that happen. 

In fact, at least at the time of writing, almost the opposite has transpired. 

But the purpose of prompt engineering is not to write beautiful prompts, to put them into books or to frame them on mantelpieces, but rather to create effective tools for getting reliable and high-quality outputs from large language models. 

Therefore, if we're going to go to the trouble of versioning and storing outputs, we should invest some at least minimal effort in doing the same for outputs. At least this is my strong contention.

## Outputs are a part of the evolving human-AI work landscape

As my own use of models evolved in 2024 and as the field moved relentlessly forward, I began to see that output storage was an important part of the picture, but not the only one. 

Just as important or perhaps more so was context, which has received attention in the form of RAG pipelines and other innovative tools. But increasingly, I'm viewing all the moving parts of effective workflows with AI as one cohesive picture. My thought then, and now, is that to reflect that, the kind of workflow tools that we require need to be interlinked in every possible way.

To give some examples to make this more concrete:

Let's take as an assumption that we *should* be storing all of our outputs ideally and ideally doing so in a system that we can robustly manage (I say this to distinguish what I envision as "proper" output management from the type of functionality seen in tools like Chat GPT and Perplexity, which are consumer-oriented, but even in their business versions, do not yet deem it necessary to provide consumers with the ability to choose where the outputs should be stored, or in which version for that matter). 

A simple feature that might seem intuitive and uncontroversial is providing the user with the ability to write their conversation history to a MongoDB or Postgres or a data warehouse like Databricks. However, trying to find this feature in today's tools would be quite an elusive rabbit hunt. This isn't to say that I've never seen these features rolled out. But that when they are, they are treated as curiosities or highly sophisticated components reserved perhaps for enterprise tier customers with assumed demanding compliance requirments.

## Output storage for knowledge retrieval

The scant attention that has been expended on creating impressive systems for routing and storing outputs to date is a pity because having a robust output storage yields value across different AI tools. 

The most basic use for it is that if users wish to retrieve information that they know was successfully derived from a high-quality prompt, then having those outputs in storage such as in a wiki is a clever way of precluding unnecessary use of prompting, thereby reducing API costs.  But from a simple human efficiency standpoint, it's also a clear winner. 

## Output storage can enable "secondary AI" on previously stored completions

At the level of information discovery and exploration, there are also lots of potential uses for secondary AI (AI on top of AI) to mine this pool of information, the generations of large language models. 

I think that this is quite a fascinating idea! It means that the (presumed) more powerful models of tomorrow can refine, summarize and better harness the generations of their earlier and less powerful predecessors, perhaps joining the dots in ways that the technology of the day was unable to do.

At a more simple level, even the technology of today can do useful things upon its own generations or that of a competitor (e.g. OpenAI summarising text created by Claude).

Trend analysis is an area within this category where the results could prove very insightful and potentially valuable:

- AI could identify fluctuations and trends over time as the organization and its users evolve in the type of prompt they send for completion. 

Gathering the outputs could also be useful for bringing this vast bank of textual data together for the purpose of fine-tuning models for the organization's internal needs, identifying the interlinking of different thoughts and topics.  These use cases could be bucketed under the internal knowledge generation category for business. 

## Output storage can enable quicker and richer context generation

But this bank of output data could also be used as the input for an automated context pipeline.

Alternatively, it might be more logical to use just the prompts in that pipeline (to feed the context store) or even use both. 

If both data were fed into a model whose sole purpose was to isolate the context-containing information from the other text, this could be a powerful way of building up a scalable context or stored in vector databases. 

## Using an output store & AI to proactively suggest agent development

Additionally, the output repository (to give a name for its totality) could be used to proactively suggest agents that the business might wish to deploy into production. 

For example, a tool could identify that there is a repetitive train of prompting which (to save time and improve efficiency) could be better handled by provisioning a focused agent. 

A proactive approach to agent generation could be a clever means for organizations to cut down on their prompting, both from a financial standpoint (reduced API costs) and from a human factors one, reducing the effort required by human prompt engineers to tailor these to each individual request.

## Simple output to context workflows

Another advantage of output storage that I have noticed is the ability to use outputs as context. 

This is more simple than the vector storage approach but involves basically saying "this was a useful output and it contained some thoughts as well as my prompt. I am going to feed that into another model as its input context and see if it can do more with that information.". This can be a very fluid workflow achieved simply by using drag and drop tools.

## Using outputs to benchmark prompt efficacy (evaluations)

The final potential benefit for storing outputs systematically is that they provide a powerful way to benchmark the efficacy of prompts against. 

By linking prompts to agent configurations and to outputs generated from them, we can do retrospective analysis determining what worked about a prompt and even compare successive versions just by seeing how the outputs changed. 

This is a great potential use-case for a simple comparative analysis, comparing the versions of an output before and after the prompt was modified to see what effect that modification had in reality. 

This supports the broad range of activity called evaluation.