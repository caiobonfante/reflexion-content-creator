from graph.graph import graph
from pprint import pprint

if __name__ == '__main__':
    res = graph.invoke(
        """
        Write a Linkedin post about Retrievel Augmented Generation (RAG).

        1. The first part should be about the hallucination problem with LLMs.
        
        2. The second part should present the RAG as a solution to the problem with a techinical 
            explanation about RAG components and how it works. Is has to present subsections for each of its components. 
            
            2.1 Embbedings 
            2.2 Retriever, 
            2.3 Vector Store
            2.4 Explain the process of how these components works together.
        
        3. The final part should present a use case of RAG in a marketing context.

        ```
        IMPORTANT: never use words/expressions like: 
            "inovative tecnique", "revolutionary", "significant improvement", "disastrous results",  
            "efficient solution" etc. 
            
            Replace them with more objective and specific words.
        ```

        Use the Philip Kotler writing style. Write as if you were explaining to a friend, in a simple, concise and clear way.
        The post should be in brazilian portuguese. 
        """
    )

    pprint(res[-1].tool_calls[0]["args"]["answer"])
    pprint(res[-1].tool_calls[0]["args"]["search_queries"])
    pprint(res[-1].tool_calls[0]["args"]["references"])