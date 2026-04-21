# Paper Summary: The Pile and Dolma (Condensed)

**Problem and Importance** 
Both The Pile and Dolma address the lack of open and diverse pretraining datasets for language models. At the time, most models were trained on proprietary datasets, preventing researchers from replicating experiments, studying how dataset composition affected model capabilities, or investigating certain issues such as bias and fairness. This slowed the porogress of language modeling reseach, allowing only large organizations to research and understang how training data affected the behaviour of models. The Pile dataset first introduced an open and diverse dataset of 800Gb of data, while Dolma expanded on the idea and created a trillion token scale dataset for models as they grew larger.

**Related Works** 
Before The Pile, open datasets pulled from only a few places, sources such as Common Crawl and C4, which was good in quality, but lacked diversity, and GitHub and PubMed, which offered quality data but were not sufficient in size for LLM training. Proprietary datasets from AI companies, which were used on most LLMs, remained undisclosed.

**Proposed Solution and Key Insight** 
The Pile combined 22 curated datasets including academic papers, code, books, web text, and conversations. The key idea was that different data sources give models different capabilities. Such as: 
- Academic text for scientific reasoning
- Code for logical thinking
- Books for long-form coherence. 
Dolma expanded on this idea with their 3 trillion tokens dataset. The researchers combined web text, code, scientific papers, Reddit, and other sources. While The Pile focused on diversity through many specialized datasets, Dolma focused on scaling up their dataset through mass extraction, filtering and deduplication.

**Drawbacks and Limitations** 
- The Pile faced copyright issues, especially with pirated books, leading to legal challenges. It was also too small at 800GB for modern models. 
- Dolma solved the size/scale problem. 
- Both datasets are heavily english focused.

**Future Research Directions** 
At the time the papers were released, legal frameworks regarding the fair use of copyright data from the internet was largely undetermined. Large web crawls will contain copyright data unfortunately, Yet, given current tools, it’s not possible to reliably or scalably detect copyrighted materials in a corpus of this
size. 
Other research directions can include extending these open datasets to other language contexts, creating better methods for measuring and reducing biases without excluding marginalized communities.