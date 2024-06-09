# Migration from On-Premises to Cloud: Challenges and Opportunities

## Overview and Goal
In this work, we conducted a systematic literature mapping to summarize the knowledge regarding the migration of legacy systems to the cloud. Additionally, we performed an exploratory analysis of discussions on Stack Overflow and other question-and-answer communities within the Stack Exchange network to gather professionals' perspectives on this topic and compare these perspectives with the knowledge found in the literature. The contributions of this study include identifying trends, patterns, advancements, gaps, challenges, and opportunities in the field of legacy system migration as reported in the literature. Most importantly, we developed a proof of concept for a decision support software tool using a Large Language Model (LLM) that provides targeted responses to questions about migrating legacy systems to the cloud, enhanced by the Retrieval-Augmented Generation (RAG) method.

## Research Questions
1. What are the challenges in migrating traditional systems to the cloud?
2. What are the opportunities in migrating traditional systems to the cloud?
3. What is the developer's perspective about the migration process?

## PICO

<p align="center">
  <img src="https://raw.githubusercontent.com/great-ufc/migration-on-premise-cloud-mapping/main/figures/PICO.png" title="PICO methodology" height="105" width="360" />
</p>

## PRISMA

<p align="center">
  <img src="https://raw.githubusercontent.com/great-ufc/migration-on-premise-cloud-mapping/main/figures/PRISMA.png" title="PRISMA results" height="316" width="346" />
</p>

## PoC Development for Legacy System Migration Decision Support Tool

This proof of concept (PoC) project assists professionals in migrating legacy systems. The architecture involves two main components:

#### 1. LLM Enhancement via RAG Method
The LLM (Llama 2) is enhanced using the Retrieval-Augmented Generation (RAG) method, which retrieves relevant content from external studies to provide more accurate responses without altering the model's core.

#### 2. Q&A System for Migration Support
A web-based Q&A system is developed where users submit questions. These questions are processed by an API that utilizes the enhanced LLM to deliver precise and relevant responses, aiding in legacy system migration.

<b>to see more about the poc click</b> <a href="https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/poc/">here</a>

## Topics Modeling with LDA algorithm

The proposed topics modeling groups the most discussed topics in the studies included in the mapping into six clusters. We use the tool <a href="https://github.com/cpsievert/LDAvis" target="_blank">LDAvis</a>.

Cluster 1 predominates, focusing on general migration to cloud issues. Next, we have cluster 2, which addresses technical topics such as coding issues, databases, networking, and more. Cluster 3 focuses on the migration process and metrics, including objectives, means, and performance evaluation. Clusters 4 and 5, due to the inter-topic distance, can be considered as a group of topics that deal with this business part, business risks, etc. Cluster 6 focuses on agile methodologies and software engineering in the cloud context.

<b>to see more about the topics modeling click</b> <a href="https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/topic%20modeling/">here</a>

## Dataset

This folder contains all the data resulting from the study:

- [``Legacy-Migration-to-Cloud-Papers.xlsx``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/dataset/Legacy-Migration-to-Cloud-Papers.xlsx): Table with the articles included and the data extraction processes for these articles. Contains the article ID and other information such as publication year, author, place of publication. It also contains the categories used in the extraction process and the results.
- [``Stack-Exchange-Exploratory-Analysis-Results.xlsx``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/dataset/Stack-Exchange-Exploratory-Analysis-Results.xlsx): Table with all queries performed on <a href="https://data.stackexchange.com/" target="_blank">Stack Exchange Data Explorer<a/>. Contains the ID, search strategy, parameters and link to reproduce.

## Docs

This folder contains the relevant documents of the study:

- [``SystematicMappingProtocol.pdf``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/docs/SystematicMappingProtocol.pdf): The Systematic Literature Mapping protocol. Contains the objectives, methods and inclusion and exclusion criteria of the study.

## Figures 

This folder contains all the visualizations used or mentioned in the article from our study:

- [``PICO.png``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/PICO.png): The figure shows the implementation of the PICO methodology used in this work.
- [``PRISMA.png``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/PRISMA.png): The figure shows the implementation of the PRISMA methodology used in the systematic mapping of this work.
- [``fig1-systematic-mapping-method.pdf``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/fig1-systematic-mapping-method.pdf): The figure shows the processes that underpinned the systematic mapping of this study.
- [``fig2-year-count.pdf``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/fig2-year-count.pdf): The figure shows a bar graph of the number of articles published per year.
- [``fig3-research-contribution-empirical.pdf``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/fig3-research-contribution-empirical.pdf): The figure presents three (3) bar graphs. Graph (a) considers the number of contribution types. Graph (b) considers the number of empirical validations. Graph (c) considers the number of research types.
- [``fig4-topics-mapped.pdf``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/fig4-topics-mapped.pdf): The figure shows the visualization of topic modeling in the LDAVis tool.
- [``fig5-challenges-and-opportunities.pdf``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/fig5-challenges-and-opportunities.pdf): The figure presents two (2) bar graphs. Graph (a) presents the number of challenges for the ten (10) established categories. Graph (b) presents the number of opportunities for the eight (8) established categories.
- [``heat-map-of-publications-per-year.pdf``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/figures/heat-map-of-publications-per-year.pdf): The figure shows a heat map of the number of articles published considering the location of the first author's affiliation.

## Tables

This folder contains all tables used or mentioned in the article from our study:

- [``table1-search-string-dabases.xlsx``](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/tables/table1-search-string-dabases.xlsx): The table of variations of the search string applied in each digital library chosen in the study.



