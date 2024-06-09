import argparse

from src.question.service import query_rag

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    
    query_text = args.query_text
    
    print(query_rag(query_text).get("formatted_response"))

if __name__ == "__main__":
    main()
