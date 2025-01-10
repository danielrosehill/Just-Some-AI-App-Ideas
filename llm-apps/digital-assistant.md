# What's That Information?

This may already exist within the purview of digital assistants, but this is a rough outline of the kind of system that I would find extremely useful. 

## The Challenge

We are all drowning in an onslaught of information. 

On any given day, we might need to keep track of:

- The numbers that we need to pick up at the post office.  
- Our To Do List for our boss.  
- What meetings we have coming up on our calendar.   
- Where that thing we're tracking on the Internet is currently.   
- What box I put that new USB hub in?  
- What the name of that organization was that I need to look into for work? 
- What's the login for that service? 
- What was the name of that cool API that I discovered? 
- What's the API key that I need for this? 
- What's my two factor authentication code for that? 
- What's my bank account number and what's its IBAN? 
- Which email did I associate with my Paypal address for the request? 

We all need so much information from so many different places that many of us find that a large part of our day is knowledge workers is derailed into fishing for these piece of information from different systems. 

 And from an information architecture standpoint to all this information needs to be "read write" - or in database terms, CRUD!
 
 We're constantly creating new small bits of information in different information repositories. 

## The Idea

Zapier et al do a great job at integrating our digital systems. We need an LLM agent building framework that specializes in integrating with everything and anything possible.  A Swiss army knife that specializes in connecting agents with data sources, but for personal users.

While some interesting systems in this regard have been developed to date, so far, much of the focus in agentic development has been on supporting enterprise use cases. Thus the focus naturally skews towards integrating agents with classic enterprise information sources like big wiki projects and databases. 

However, I believe that these tools could be just as, if not more transformative for personal users.  

## Implementation

The trick here would be to create not only an integration platform, but a front end for users to actually engage with.  

 A challenge in the LLM/AI agent tools that have been developed so far, I believe, is that they segregate between development platforms and front ends for users. 
 
 While this might be logical, especially in the context of business bots, this also puts these tools out of reach for ordinary consumers. Most people want to use these tools, not get tools that they then need to embed in their own custom built front ends!

 ## Feasibility / Integrations

 Another thing that ordinary consumers do not want to get involved with is the complexity of things like embedding and vectorizing data To turn things like documents into data stories that are optimized for retrieval by LLM agents. 
 
 I think that an effective tool for organizing consumers needs to keep this abstracted and under the hood. 

 I think that the best approach would be to have an internal context management system for users. Perhaps there could be a discovery feature whereby the user connects a drive and then it picks out things like "hey, I see that your zip code is X". But for an MVP/POC, It might be easier to just have a deliberately populated context library with a simple key value store for inputting common nuggets of information. 

 Much of the information that I think would be helpful for consumers to easily retrieve through assistance would be classed as personally identifiable information. You might want to say, hey, I want to send something to my in law. Can you get me their address quickly? So there might be some data governance and compliance questions here too. 

## Agent Framework

Beyond setting up the connections, the user would want to configure the agents to actually engage with.

I think that a UI element that often goes underdeveloped in these platforms is the ability to switch quickly between a large network of agents. 

Voice integration would be important too. Both robust STT and TTS and the ability to have speech to speech would also be a big advantage. 

## Value Add / Differentation

The problem was the major digital assistance platforms today is that they tend to be developed by vendors like Google with well established ecosystems who (often) want to use them as a way to ring fence customers enter their own ecosystems. 

But this goes against what many customers are actually looking for. I reckon that many people would prefer digital assistants that are vendor agnostic, especially those that are more privacy conscious and want to decouple the assistant from the rest of their. Information architecture.

What I think would be required, and what would be valuable is to clearly distinguish this from all the enterprise agent ecosystems that are out there. Emphasis on integration with home assistant projects would also be particularly useful in this respect.  

But the primary focus would be on integracing with SaaS and hybrid personal infrastructure. 

## Context Development

Another feature that I think would be really useful, and which hasn't been seen much is the ability to use agents in order to proactively develop contextual data - an approach I have been experimenting with for my own use.

The implementation which I have been using so far is something like having an agent to ask you questions to develop context for a specific purpose.  

Or perhaps this context could be gamified or made a little bit more enjoyable for end users. Using a real time speech to speech interaction or in the AI of tomorrow, a real time video chat with an avatar, Users could be nudged into answering questions about specific topics, and then that context data could be stored in the system to enhance the personalization of the agents. 

If this were coupled with a reverse system - mining a conversation history and feeding those into a vector storage (ie, a RAG pipeline running the other way), the utility of this feature could be enhanced further.  
 