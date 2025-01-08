# Some fun experiments in context for personal use!

08-Jan-25

*Captured with speech to text, lightly edited for clarity*

The other theme in large language model use that captivated my intention in 2024 (and which I'm therefore writing a note about in early 2025!) was the question of context management. 

My interest in context management is a little different than the type of use that many are excited about for this technology. 

Much of the interest in context in 2024 to date has been around its ability of vector storage and embeddings to allow organizations to capture their internal data in a way that is easily retrievable by large language models. 

This can serve the purpose of grounding their responses or providing them with access to data beyond their training periods. These are very exciting use cases and have many potential applications in the business world and are increasingly served by lots of frameworks and tools of every kind. However, I think that the potential of context to make large language models much more useful for personal users is being hugely overlooked.

## Even "small context" can improve LLM outputs significantly!

My humble experiments in 2024 with context management involved as a very first way of testing out their use, creating a simple GitHub repository which I called my "context repo" (setting one up for work and personal use) and populating them with simple markdown documents containing simple pieces of context. 

The first example that I found extremely helpful was a context document describing the hardware of my computer. 

As a Linux user who enjoys sometimes updating my hardware, it can be challenging to identify new components because doing so involves multiple dependencies: the type of RAM needs to be compatible with the motherboard, there has to be enough power in the computer to supply it, it has to fit within the form factor, etc. 

While it's true that there are online tools specifically for compatibility checking that do this, it was quite revelatory to see that a standard large language model could do essentially the same work, just supplied with a little markdown file containing nothing more than about 20 lines of data about what I had running in the computer.

## What other personal context data could be helpful?

This little experiment really got me thinking what other small chunks of context users could selectively drop into repositories (and frontends) to ground their outputs and enhance enormously the specificity and personalisation of their responses.

The bank of examples that I found have ranged from potentially highly useful to simply a little bit amusing. 

For example, while there are specific AI tools being marketed to help users find movie recommendations, I found that you can do pretty much as good a job, if not better, by simply dictating what kind of movies you enjoy watching into a microphone, using Whisper to transcribe that to text, and then uploading that into a vector store connected to one of your agents. 

Alternatively, and more simply, you could simply take that markdown file after cleaning it up a bit and then drag and drop it into a LLM of any variety (offline or locally hosted) and prompt "these are my interests in movies, can you think of anything good on Netflix I might enjoy tonight?" (requirements: real time data or Netflix RAG!).

## Scaling up personal context generation

These little experiments have been my own proof of concept for exploring the idea of how context can enhance outputs. But I've also been drawn to the question of how can we make this process more scalable and more robust? 

This is not a simple question because even tools like the mighty Chat GPT are currently only rolling out their first features for preserving memory "infinitely" (across chats). 

One potential approach to this idea is creating a pipeline whereby the prompts and outputs the user sends to models and the data received back are fed into a AI tool which can then isolate the context. 

Contextual data isn't quite static - rather it contains a mixture of immutable data and data that might be always evolving. Our place of birth is an example of the former, but whether we're looking for a new job or not is an example of the latter. At some points in our life "yes" at other points "no". Therefore, I believe that a robust context data system for personal use needs to transcend the read-only limitation that we see in some agentic workflows. It should ideally be read-write! Some data needs to be deleted, some context data needs to be updated, and additional context needs to be added as our lives progress.

## Deliberate approaches for generating personal context data

The second idea that I've been thinking about for generating personal context data to feed into models is the idea of trying to actually architect this process more deliberately.

I've experimented with a few methods and those are some of the repositories that I've added to GitHub during the last calendar year.

- One of my ideas was creating an agent whose sole purpose was isolating context from data. You could ramble on for 10 minutes talking about what you feel about IKEA furniture to whether or not you like your latest headphones and the agent could simply parse that information picking out the relevant context data, perhaps rewriting it in the third person, and reformatting it as JSON. 
- 
The second idea to using agents to streamling context generation was deploying an agent tasked with asking you questions about a specific area (the agent is instructed that its job is helping the user to generate context for the purpose of creating a richer vector store for enhancing LLM outputs.)

In this second workflow, the user might tell the agent that, "hey, I'd like you to give me some questions that will help me to build up a context repo for a job search". The agent may then begin asking the user questions like, "what are your career aspirations?" "what kind of workplace do you like, what have been some work experiences you did not enjoy?" and then generate the context data based upon the user's responses. 

This more deliberate approach might be more effective in more selective LLM workflows - for example, if the user were developing specific vector stores tied to specific assistants for specific purposes. 

There are probably many ways to go about achieving this, and these thoughts and initial ideas or just to lay down some coherence to the ideas I will be working on this year and beyond.