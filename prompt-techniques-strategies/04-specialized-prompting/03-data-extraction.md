# Data Extraction Prompting

## Overview

Data extraction prompts convert unstructured text into structured formats. This module covers techniques for reliable information extraction with consistent output formats.

## Extraction Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                   DATA EXTRACTION PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   UNSTRUCTURED TEXT                                             │
│         │                                                        │
│         ↓                                                        │
│   ┌─────────────────────────┐                                   │
│   │  IDENTIFY ENTITIES      │                                   │
│   │  (names, dates, etc.)   │                                   │
│   └─────────────────────────┘                                   │
│         │                                                        │
│         ↓                                                        │
│   ┌─────────────────────────┐                                   │
│   │  EXTRACT VALUES         │                                   │
│   │  (normalize format)     │                                   │
│   └─────────────────────────┘                                   │
│         │                                                        │
│         ↓                                                        │
│   ┌─────────────────────────┐                                   │
│   │  STRUCTURE OUTPUT       │                                   │
│   │  (JSON, CSV, etc.)      │                                   │
│   └─────────────────────────┘                                   │
│         │                                                        │
│         ↓                                                        │
│   STRUCTURED DATA                                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Extraction Patterns

### Pattern 1: Entity Extraction

```
Extract all entities from the following text:

TEXT:
{text}

ENTITY TYPES TO EXTRACT:
- PERSON: Names of individuals
- ORGANIZATION: Company, institution names
- LOCATION: Cities, countries, addresses
- DATE: Dates and time references
- MONEY: Currency amounts
- PRODUCT: Product or service names

OUTPUT FORMAT (JSON):
{
  "entities": [
    {
      "text": "extracted text",
      "type": "ENTITY_TYPE",
      "start": character_offset,
      "end": character_offset,
      "normalized": "standardized form if applicable"
    }
  ]
}

RULES:
- Include all instances, even duplicates
- Normalize dates to ISO format (YYYY-MM-DD)
- Normalize money to numeric with currency code
- If entity type is uncertain, use best guess with confidence
```

### Pattern 2: Form/Document Extraction

```
Extract information from this document:

DOCUMENT:
{document_text}

SCHEMA:
{
  "invoice_number": "string",
  "date": "ISO date string",
  "vendor": {
    "name": "string",
    "address": "string",
    "contact": "string or null"
  },
  "customer": {
    "name": "string",
    "address": "string"
  },
  "line_items": [
    {
      "description": "string",
      "quantity": "number",
      "unit_price": "number",
      "total": "number"
    }
  ],
  "subtotal": "number",
  "tax": "number",
  "total": "number"
}

RULES:
- Use null for missing optional fields
- Use empty array for missing lists
- Normalize all numbers to decimal format
- Dates to ISO 8601 format
- If value is unclear, add "_uncertain": true flag

OUTPUT: Valid JSON matching the schema exactly.
```

### Pattern 3: Relationship Extraction

```
Extract relationships between entities in this text:

TEXT:
{text}

RELATIONSHIP TYPES:
- WORKS_FOR: Person works for Organization
- LOCATED_IN: Entity located in Location
- OWNS: Entity owns Entity
- PARTNERED_WITH: Organization partnered with Organization
- REPORTED_BY: Event reported by Source

OUTPUT FORMAT:
{
  "relationships": [
    {
      "subject": "entity name",
      "subject_type": "ENTITY_TYPE",
      "relation": "RELATIONSHIP_TYPE",
      "object": "entity name",
      "object_type": "ENTITY_TYPE",
      "confidence": 0.0-1.0,
      "evidence": "quote from text supporting this"
    }
  ]
}

RULES:
- Only extract explicitly stated relationships
- Include confidence score
- Provide text evidence for each relationship
```

### Pattern 4: Event Extraction

```
Extract events from this news article:

ARTICLE:
{article_text}

EVENT SCHEMA:
{
  "events": [
    {
      "type": "event category",
      "description": "brief description",
      "date": "when it occurred",
      "location": "where it occurred",
      "participants": ["involved parties"],
      "outcome": "result or impact",
      "source_quote": "relevant quote from article"
    }
  ]
}

EVENT TYPES:
- ANNOUNCEMENT: New product, policy, statement
- TRANSACTION: Purchase, sale, merger
- INCIDENT: Accident, crime, disaster
- APPOINTMENT: Hiring, promotion, resignation
- LEGAL: Lawsuit, ruling, regulation

Extract all events mentioned, even if briefly.
```

## Structured Output Formats

### JSON Extraction

```
Extract data and output as valid JSON:

TEXT:
{text}

JSON SCHEMA:
{schema}

REQUIREMENTS:
- Output ONLY valid JSON, no markdown code blocks
- Match schema exactly
- Use null for missing values
- Use empty arrays for empty lists
- Escape special characters in strings
- Numbers as numeric types, not strings

VALIDATION:
Before outputting, verify:
[ ] JSON is syntactically valid
[ ] All required fields present
[ ] Types match schema
[ ] No extra fields added
```

### Table/CSV Extraction

```
Extract tabular data from this text:

TEXT:
{text}

EXPECTED COLUMNS:
- Name
- Date
- Amount
- Category
- Notes

OUTPUT FORMAT:
CSV with header row, properly quoted fields

RULES:
- First row: column headers
- One row per record
- Quote fields containing commas
- Escape quotes within fields
- Use empty string for missing values
- Dates in YYYY-MM-DD format
```

### Key-Value Extraction

```
Extract key information as key-value pairs:

TEXT:
{text}

FIELDS TO EXTRACT:
- company_name (required)
- founded_year (optional)
- headquarters (optional)
- ceo_name (optional)
- employee_count (optional)
- annual_revenue (optional)
- industry (required)
- stock_symbol (optional)

OUTPUT FORMAT:
{
  "field_name": "extracted_value",
  "field_name_confidence": 0.0-1.0
}

RULES:
- Include confidence for each extraction
- Normalize numeric values (remove commas, convert M/B to numbers)
- Return null for not found (with confidence 0)
- If multiple values found, use most recent/authoritative
```

## Handling Extraction Challenges

### Ambiguous Values

```
When extracting from text, handle ambiguity as follows:

AMBIGUITY HANDLING:
1. Multiple possible values:
   - List all options with confidence scores
   - Select highest confidence for primary value

2. Conflicting information:
   - Note the conflict
   - Prefer more recent/authoritative source
   - Flag for human review

3. Incomplete information:
   - Extract what's available
   - Mark incomplete fields
   - Note what's missing

OUTPUT FORMAT for ambiguous cases:
{
  "field": "primary_value",
  "field_confidence": 0.8,
  "field_alternatives": [
    {"value": "alt_value", "confidence": 0.5}
  ],
  "field_notes": "explanation of ambiguity"
}
```

### Missing Data

```
Handle missing data during extraction:

FOR EACH FIELD:
- If found: Extract and include
- If not found: Set to null
- If partially found: Extract partial, flag as incomplete

OUTPUT METADATA:
{
  "extraction_status": {
    "complete_fields": ["field1", "field2"],
    "missing_fields": ["field3"],
    "partial_fields": ["field4"],
    "confidence_overall": 0.85
  },
  "data": {
    // extracted data
  }
}
```

### Normalization Rules

```
Apply these normalization rules during extraction:

DATES:
- Input: "Jan 5, 2024", "5/1/24", "2024-01-05"
- Output: "2024-01-05" (ISO 8601)

CURRENCY:
- Input: "$1,234.56", "1234.56 USD", "$1.2M"
- Output: {"amount": 1234.56, "currency": "USD"}

PHONE NUMBERS:
- Input: "(555) 123-4567", "555-123-4567"
- Output: "+15551234567" (E.164 format)

PERCENTAGES:
- Input: "50%", "0.5", "fifty percent"
- Output: 0.5 (decimal)

NAMES:
- Input: "John Smith", "Smith, John", "J. Smith"
- Output: {"first": "John", "last": "Smith"}

ADDRESSES:
- Parse into: street, city, state, postal_code, country
```

## Few-Shot Extraction

```
Extract contact information following these examples:

EXAMPLE 1:
Input: "Contact John Smith at john@example.com or call 555-123-4567"
Output: {
  "name": "John Smith",
  "email": "john@example.com",
  "phone": "+15551234567"
}

EXAMPLE 2:
Input: "For inquiries, email support@company.com"
Output: {
  "name": null,
  "email": "support@company.com",
  "phone": null
}

EXAMPLE 3:
Input: "Reach Jane Doe (jane.doe@corp.net) at extension 5678"
Output: {
  "name": "Jane Doe",
  "email": "jane.doe@corp.net",
  "phone": "ext. 5678"
}

NOW EXTRACT:
Input: {new_text}
Output:
```

## Validation and Quality

```
After extraction, validate results:

VALIDATION CHECKS:
1. Schema compliance - All required fields present
2. Type correctness - Values match expected types
3. Format validation - Dates, emails, phones in correct format
4. Range checks - Numbers within reasonable bounds
5. Consistency - Related fields are consistent

OUTPUT:
{
  "extracted_data": {...},
  "validation": {
    "passed": true/false,
    "errors": [
      {"field": "field_name", "error": "description"}
    ],
    "warnings": [
      {"field": "field_name", "warning": "description"}
    ]
  }
}
```

## Best Practices

1. **Define schema precisely** - Exact field names and types
2. **Provide examples** - Show expected extraction format
3. **Handle edge cases** - Missing, ambiguous, malformed data
4. **Validate output** - Verify JSON validity and schema compliance
5. **Include confidence** - Know which extractions are uncertain

## Next Steps

- [04-reasoning-tasks.md](04-reasoning-tasks.md) - Analytical prompts
- [../05-optimization/01-prompt-debugging.md](../05-optimization/01-prompt-debugging.md) - Debugging prompts
