from PySide6.QtCore import QThread, Signal
from openai import OpenAI
from typing import Dict, Optional, List, Union, Any

class ModelManager:
    def __init__(self):
        self.models: Dict[str, dict] = {}
        self.current_model: Optional[str] = None
        self.api_key: Optional[str] = None
        
    def register_model(self, name: str, provider: str, base_url: str):
        """Register a new model configuration"""
        self.models[name] = {
            'provider': provider,
            'base_url': base_url
        }
        
    def set_current_model(self, name: str):
        """Set the currently selected model"""
        if name in self.models:
            self.current_model = name
            
    def set_api_key(self, key: str):
        """Update the API key"""
        self.api_key = key
            
    def get_config(self) -> dict:
        """Get current model configuration"""
        if not self.current_model:
            raise ValueError("No model selected")
            
        return {
            'name': self.current_model,
            **self.models.get(self.current_model, {}),
            'api_key': self.api_key
        }

    def clear_models(self):
        """Clear all registered models"""
        self.models.clear()
        self.current_model = None
    
    def preset_llm_model(self, provider: str):
        
        
        
        
        return
        
        
class LLMWorker(QThread):
    """
    Worker thread for handling LLM API calls.
    Emits signals for new content chunks and status updates.
    """
    new_content = Signal(str)
    started_signal = Signal()
    finished_signal = Signal()
    # Flag to stop generation
    _stop = False

    def __init__(self, model_manager: ModelManager, messages=None):
        super().__init__()
        self.model_manager = model_manager
        self.messages = messages
        self.client = None
        self._should_stop = False

    def _init_client(self):
        """Initialize the OpenAI client with configuration from ModelManager"""
        # current_model = self.model_manager.current_model
        current_model=self.model_manager.get_config()
        self.client = OpenAI(
            api_key=self.model_manager.api_key,
            base_url=current_model["base_url"] if current_model else None
        )

    def run(self):
        """Execute the LLM API call and emit results"""
        self._stop = False
        self.started_signal.emit()
        
        self._init_client()
        config = self.model_manager.get_config()
        
        if not self.client or not self.messages:
            self.finished_signal.emit()
            return
            
        # Check if we're using a vision model
        is_vision_model = config['name'] == 'qwen-vl-plus'
        
        # Prepare messages for the API call
        api_messages = []
        for msg in self.messages:
            # Handle special content format for vision models
            if is_vision_model and isinstance(msg.get('content'), list):
                # This is already in the correct format for vision models
                api_messages.append(msg)
            else:
                # Standard text message
                api_messages.append(msg)
        
        try:
            # Make the API call
            response = self.client.chat.completions.create(
                model=config['name'],
                messages=api_messages,
                stream=True,
            )
        
            for chunk in response:
                if self._stop:
                    break
                if chunk.choices[0].delta.content:
                    self.new_content.emit(chunk.choices[0].delta.content)
        except Exception as e:
            # Handle any errors during API call
            self.new_content.emit(f"Error: {str(e)}")
        finally:
            self.finished_signal.emit()

    def stop(self):
        """Stop the generation process"""
        self._stop = True
