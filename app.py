import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_article(keyword):
    """
    Generate a long-form SEO article based on the given keyword.
    """
    # Create a detailed prompt for the article
    prompt = f"""Write a comprehensive, SEO-optimized article about {keyword}. 
    The article should:
    - Be well-structured with clear headings and subheadings
    - Include an engaging introduction
    - Provide detailed, valuable information
    - Be approximately 1500 words
    - Use natural language and maintain good readability
    - Include a conclusion
    
    Format the article with proper markdown formatting."""

    try:
        # Generate the article using GPT-4
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert content writer skilled in creating SEO-optimized articles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2500
        )
        
        # Extract and return the generated article
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating article: {str(e)}"

def main():
    # Get keyword input from user
    keyword = input("Enter your SEO keyword or topic: ")
    
    print("\nGenerating article...")
    article = generate_article(keyword)
    
    # Save the article to a markdown file
    filename = f"article_{keyword.lower().replace(' ', '_')}.md"
    with open(filename, 'w') as f:
        f.write(article)
    
    print(f"\nArticle has been generated and saved to {filename}")

if __name__ == "__main__":
    main()