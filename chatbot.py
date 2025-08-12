import chainlit as cl
from app import qa_bot  # Assuming qa_bot() is in app.py as you described.

@cl.on_chat_start
async def start():
    # Initialize the QA chain from the previously defined qa_bot function
    chain = qa_bot()
    
    # Send a starting message to the user
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi there, welcome to the Medical Bot. Please enter your query below."
    await msg.update()

    # Save the chain in the user session
    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message: cl.Message):
    # Retrieve the chain stored in the user session
    chain = cl.user_session.get("chain") 
    
    # Setup callback handler to stream final answer and process results
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True
    
    # Process the incoming message
    res = await chain.acall(message.content, callbacks=[cb])
    answer = res["result"]
    sources = res["source_documents"]

    # Include sources if found, else indicate no sources
    if sources:
        answer += "\nSources: Extracted from trusted medical references."
    else:
        answer += "\nNo sources found."

    # Send the answer back to the user
    await cl.Message(content=answer).send()
