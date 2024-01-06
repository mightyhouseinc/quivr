from fastapi import HTTPException
from llm.utils.extract_api_definition import format_api_brain_property
from llm.utils.sanitize_function_name import sanitize_function_name
from modules.brain.entity.brain_entity import BrainEntity
from modules.brain.service.api_brain_definition_service import ApiBrainDefinitionService

api_brain_definition_service = ApiBrainDefinitionService()


def get_api_brain_definition_as_json_schema(brain: BrainEntity):
    api_brain_definition = api_brain_definition_service.get_api_brain_definition(
        brain.id
    )
    if not api_brain_definition:
        raise HTTPException(
            status_code=404, detail=f"Brain definition {brain.id} not found"
        )

    required = []
    required.extend(api_brain_definition.params.required)
    required.extend(api_brain_definition.search_params.required)
    api_properties = (
        api_brain_definition.params.properties
        + api_brain_definition.search_params.properties
    )

    properties = {
        property.name: format_api_brain_property(property)
        for property in api_properties
    }
    parameters = {
        "type": "object",
        "properties": properties,
        "required": required,
    }
    return {
        "name": sanitize_function_name(brain.name),
        "description": brain.description,
        "parameters": parameters,
    }
