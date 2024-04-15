def generate_summary_prompt(page):
    # Start with the page title and summary
    prompt = (
        f"Generate an advanced summary for the Wikipedia page titled '{page.title}'. The summary of the page is as "
        f"follows: '{page.summary}'. ")

    # Add the URL of the page
    prompt += f"The page can be accessed at this URL: '{page.fullurl}'. "

    # Check if the page exists
    prompt += "The page exists. " if page.exists() else "The page does not exist. "

    # Add the sections of the page
    if page.sections:
        prompt += f"Here are the sections of the page: {', '.join([s.title for s in page.sections])}. "
        # Fetch more details for each section if available
        for section in page.sections:
            # Include a placeholder for providing detailed information about the section
            prompt += (f"Provide detailed information about the '{section.title}' section."
                       f"Explain the content and relevance of the section in the context of the page."
                       f"Analyze the importance of the section in the overall structure of the page."
                       f"Describe how the section contributes to the page's main topic."
                       f"Summarize the information found in the section in detail."
                       f"Discuss the key points and arguments presented in the section."
                       f"Explain how the section is organized and structured."
                       f"Analyze the impact of the section on the reader's understanding of the page."
                       f"Provide examples or illustrations from the section to support your explanation.")

    # Add the categories of the page
    if page.categories.values():
        prompt += f"The page belongs to the following categories: {', '.join([c.title for c in page.categories.values()])}. "
        # Fetch more details for each category if available
        for category in page.categories.values():
            # Include a placeholder for explaining more about the category
            prompt += (f"Explain more about the '{category.title}' category."
                       f"Describe the importance of the category in the context of the page."
                       f"Analyze how the category is related to the page's content."
                       f"Discuss the relevance of the category to the page's main topic."
                       f"Provide examples or illustrations from the category to support your explanation."
                       f"Explain how the category contributes to the reader's understanding of the page."
                       f"Analyze the impact of the category on the page's content."
                       f"Discuss how the category is used to organize information on the page."
                       f"Explain the significance of the category in the broader context of the page's subject matter."
                       f"Summarize the information found in the category in detail."
                       f"Discuss the key points and arguments presented in the category."
                       f"Explain how the category is structured and organized."
                       f"Analyze the impact of the category on the reader's understanding of the page."
                       f"Provide examples or illustrations from the category to support your explanation.")


    # Add the links in the page
    if page.links.values():
        prompt += f"The page contains the following links: {', '.join([link.title for link in page.links.values()])}. "
        # Fetch more details for each link if available
        for link in page.links.values():
            # Include a placeholder for providing additional information about the link
            prompt += (f"Provide additional information about the '{link.title}' link and its relevance to the page."
                       f"Explain how the link is related to the page's content."
                       f"Describe the importance of the link in the context of the page."
                       f"Analyze the impact of the link on the page's content."
                       f"Discuss how the link contributes to the reader's understanding of the page."
                       f"Provide examples or illustrations from the link to support your explanation."
                       f"Explain the significance of the link in the broader context of the page's subject matter."
                       f"Summarize the information found in the link in detail."
                       f"Discuss the key points and arguments presented in the link.")

    # Add the language links of the page
    if page.langlinks.items():
        prompt += f"The page has language links to other Wikipedia pages: {', '.join([f'{k}: {v.title}' for k, v in page.langlinks.items()])}. "
        # Fetch more details for each language link if available
        for language, link in page.langlinks.items():
            # Include a placeholder for explaining more about the content in the linked language
            prompt += f"Explain more about the content in '{language}' language linked to '{link.title}'. "

    # Request an advanced summary
    prompt += (
        "Please provide an advanced summary of this page. Use your capability to explain as much as you can about the "
        "summary."
        "Tell me everything in deep detail, considering its content, structure, and relevance. "
        "Include an analysis of the page's main points, its organization, and its relevance to different types of "
        "users."
        "Also, summarize the information found in the page's sections, categories, links, and language links in detail."
        "Discuss the key points and arguments presented in the page and how they contribute to the reader's "
        "understanding."
        "Analyze the impact of the page on the reader's knowledge and provide examples or illustrations to support "
        "your explanation.")

    return prompt
