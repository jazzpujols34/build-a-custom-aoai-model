# Fine-Tuning OpenAI ChatGPT with Azure and MediaWiki API

This project provides an example of how to fine-tune the Azure OpenAI Service model using MediaWiki API. The example demonstrates how to use the MediaWiki API to fetch a title and generate the first sentence of the title.

## Prerequisites

- Python 3.6 or later

- An Azure account

- An OpenAI account

- Python packages: `openai`, `beautifulsoup4`, `requests`, `python-dotenv`

## Setup

1. Clone the repository to your local machine.

2. Install the required Python packages using pip:

```
 pip install -r requirements.txt
```

3. Set up your environment variables in a `.env` file:

```
OPENAI_API_BASE=<your-openai-api-base>
OPENAI_API_KEY=<your-openai-api-key>
```

## Usage

Run the `chatgpt_fine-tune.py` script:

```
python chatgpt_fine-tune.py
```

The script will:

1. Fetch random titles from Wikipedia using the MediaWiki API.

2. Generate a summary for each title by scraping the corresponding Wikipedia page.

3. Create a training dataset and a validation dataset from these summaries.

4. Upload the datasets to Azure OpenAI for fine-tuning the ChatGPT model.

## Datasets

The `training.jsonl` and `validation.jsonl` files contain the training and validation datasets, respectively. Each line in these files is a JSON object that represents a single training example, with a "prompt" field (the title) and a "completion" field (the summary).

## Fine-Tuning

The script uses the Azure OpenAI CLI to upload the datasets and start the fine-tuning process. You can check the status of the training and validation files by calling the `check_status` function with the IDs of the training and validation files.

## Contributing

Contributions are welcome. Please open an issue to discuss your ideas or submit a pull request.

## License

This project is licensed under the terms of the MIT license.
