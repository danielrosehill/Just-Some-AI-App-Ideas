# My LLM - Personalised LLM Framework

## The Challenge

Out of the box, large language models are generalist information tools. 

As agent capabilities mature and advance quickly, the main approach to making them more personalized is by connecting them to external information sources, for instance by API integrations. 

To date, most of the focus in AI assistants and agents Has been in the business use cases. These provide compelling ways for companies to reduce human effort in internal tasks, and they have been widely deployed in things like customer service too. 

I am much more enthusiastic, however, about their potential to help individual users in their personal lives or in their personal jobs. The second use case is not synonymous with enterprise use of agents, because it might involve users just using these tools to perform their own functions. 

In the course of my own experimentation with large language models, I seem compelling proof that small contextual data can be leveraged extremely effectively to make large language models essentially personalized and vastly more powerful and useful. 

A simple example to illustrate is a single markdown file containing my operating system and the hardware in my customized desktop computer. It's a single markdown file of about 20 lines. By providing this selectively into any large language model, I can quickly provide it with all the context it needs to suggest hardware upgrades. 

## Personal Context Management Area

I don't think that users should have to choose between whether they want to enhance the functionality of their models through API integrations or by connecting them to personal context data stores. 

In fact, I think that they serve separate and complementary purposes. 

The first grounds the models in the personal information relevant to the users. The second opens the door for them not only to gain additional information, but also to conduct agentic functions. 

The methodology that I've used for developing my own personal context libraries is one I believe that could be employed effectively into any framework designed for this purpose. 

There's a context area in which the user can create pools of contextual knowledge about specific subjects. Let's say one is our food and drink preferences. The other is their preferences and entertainment. Another is their financial objectives, another is their career objectives. 

To make it easier to allow agents to connect to multiple sources and to federate use in an organizational setting these could be grouped into collections. 

As it would be tedious to connect a single agent to 20 different context data pools, the aforementioned data stores for entertainment and food preferences could just be bundled into one master data pool called Personal Context Data.

But separating these into their constituent elements makes it easier for users to focus on developing context data in one pool at a time. 

Having experimented with this myself, generating personal context data deliberately is a bit of a strange experience.  The methodology I have employed to date is simply using speech to text dictation and recording voice notes where I describe my preferences in certain things. 

The personal context data could be far more granular. You might have a context file with personal particulars that includes things like the user zip code and place of residence. The process for updating these could be the same as managing any key value pair. 

I believe that a gamification process could be employed by leveraging a agent to play the role of context data gathering bot, which I've also used successfully. 

The agent is told that its purpose is to help the user to develop these personal context data stores, and then to ask the user questions guided towards the type of context data they're developing. This modelled interview mechanism makes the process of generating these feel a bit more natural and logical. 

## The Finished Product

The purpose of this product would be to create an agent framework that is honed in on the purpose of personal LLM - contextualizing large language model assistance for personal rather than business use cases. 

In more advanced implementations, the RAG pipeline could be a two way process - users could deliberately create contextual data for input into the RAG pipeline in the method I described above. Or it could work the other way around: The conversation history is parsed for context data and that is then automatically piped into the pipeline. This is more like a memory store. Both could be used in conjunction to deliver the best results. 

## Frontend

It would be vital that this is not only a configuration tool for setting up the context data on the agents, but also one for actually using them. Some frameworks focus on just doing the latter, and I think that it makes them far less valuable for end users. 

While this idea might appeal initially to more technically inclined users, over time I think that the concept of personalizing large language model tools will become much more mainstream. Therefore, I think the tool would need to provide a front end for using the configured agents and switching between them quickly, and not just for configuring the parameters. 

With selective integrations to Software as a Service tools and the bank of context data supplied through the tool itself, users would be able to access a very personalized LLM experience. 