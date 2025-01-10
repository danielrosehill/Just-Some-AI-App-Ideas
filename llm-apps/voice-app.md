# Voice LLM App Idea

## The Challenge

We get out of AI systems like large language models what we put in. 

As models become increasingly more powerful and more capable, the traditional limitations around context length are becoming less relevant. 

Models with more powerful reasoning capabilities are able to effectively handle longer prompts without the quality of the inference substantially degrading. 

This opens the door to users to provide much richer and detailed prompts with lots of context data. This could potentially be a way to obviate much of the need for RAG pipelines and injecting context through that mechanism -  rather than focusing on preloading context into models, we make them better at parsing it on the fly, enhancing their core capabilities rather than working on an accompanying technology. 

The only way that I've been able to adopt voice prompting in my personal use of AI tools, however, is by leveraging speech to text and voice dictation. At the cost of introducing some uncharacteristic typos that sometimes pose challenges to inference enable to much more easily and more effectively prompt at the kind of length that yields much better results for AI systems. 

Whenever I explore AI tools for voice, however, I notice that there is a big tendency to focus these tools on hands free operation. 

I think that this ignores the workflow of tomorrow, in which those who embrace voice will do so in all contacts, both when they're at work and when they're on the go. IE. I believe that voice LLM tools need to function well across both desktop and mobile environments, and ideally to provide a consistent functionality for the end user.

## STT, TTS, STS

There are various ways in which you can use voice to interact with AI systems currently. I think that an ideal system needs to be able to cater to all of them to reflect the different ways in which users might want to interact with the same system. 

For example:

- When I am working on my computer, I favor using speech to text to write prompts, but I then like to read those prompts on my screen because of the context I'm in. So in this use case I'm doing speech to speech for prompting and then I'm simply using conventional output generation (text from chat AI in a chatbot).

- When I'm using an AI tool out of the house however, I don't read on the screen because it's distracting from my environment.  In this context, speech to speech is probably the most useful. But the current implementation of speech to speech in real time APIs does not support the kind of prompting that I like to do very well (the AI responds too quickly!). For the tool to work with my kind of prompting, I'm missing the feature of being able to say something like "I'm finished, send prompt" so that I can take my time over wording what I'm looking for. For this reason, at the current time, STT and TTS paired together become more relevant on the mobile context to support my kind of use.   

## Output Storing & Routing

The facet of my personal use of large language models, which might distinguish me from some users, but I don't think from all of them, is that I pay particular attention to what I do was the outputs that are generated. 

When I am at the desktop computer and if I get a good quality output that I think might have later utility, I store it into a notepad, generating in the course of doing so my own personal wiki from AI generated content. 

Sometimes I capture just an output. In other instances I capture my prompt and my output. 

I use this information later to develop my prompt library and to retrieve and discover information that I previously received from AI systems. Increasingly, secondary AI systems in which AI tools work on top of a bank of outputs from other AI tools drive additional and very important value. 

In the context of a voice AI tool that supports business and personal users, or those using the same tool for both instances, I think that the ability to route outputs would be very important. 

MCP and agenetic frameworks that are capable Of interacting with other systems are becoming quickly, more mature and available. In the hands free / mobile version of this implementation I think that this would be particularly valuable and essential. 

The idea I have is for integrating voice commands into the app itself so that users don't have to rely upon the often limited availability of command words in digital assistants embedded into smartphone systems. 

Let's say that a business user is interacting with the large language model in a mobile hands free context. After writing a prompt they get a couple of responses from the AI tool. And after some iteration they get an output that is something like a finished version. Let's imagine in this situation that the user is using the AI tool to develop an agenda for a forthcoming meeting. 

In this context, the user might wish to capture the last of these outputs into a a couple of business systems: 1) Let's save this into our Google Drive and 2) Let's send this by email to the meeting participants. 

In this example, both of these functionalities would be highly valuable. But for desktop users they would be extremely helpful too - it's just that desktop users have traditional tools to rely upon as a backup. But my belief is that ultimately voice commands and voice centric input will dominate across contexts, so it would be a mistake to neglect integrating these tools well into a desktop version. 

A feature that I feel is missing from many large language model front ends at the moment is storing all the outputs into a database. Given that textual content is extremely lightweight and file size, I think it would be valuable to do this whether the selective output routing is configured as an option or not. 

In the enterprise use case, for compliance reasons, organizations might wish to have the full chat history that a user uses with a company developed agent right into a data warehouse for perhaps further information mining, although this might raise some compliance and data governance bligations that would make adding this not worthwhile.