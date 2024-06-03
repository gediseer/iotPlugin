import re
import subprocess
from typing import AsyncIterator

from miservice import MiIOService, MiNAService, miio_command

from xiaogpt.config import Config
from xiaogpt.tts.base import TTS
from xiaogpt.utils import calculate_tts_elapse


class MiTTS(TTS):
    def __init__(
        self, mina_service: MiNAService, device_id: str, config: Config
    ) -> None:
        super().__init__(mina_service, device_id, config)
        self.miio_service = MiIOService(mina_service.account)

    async def say(self, text: str) -> None:
        if not self.config.use_command:
            try:
                await self.mina_service.text_to_speech(self.device_id, text)
            except Exception:
                pass
        else:
            await miio_command(
                self.miio_service,
                self.config.mi_did,
                f"{self.config.tts_command} {text}",
            )
    async def run_cmd(self, cmd):  
        # 定义命令字典  
        cmd_dict = {  
            'cmd1': 'python ..\MiService\micli.py -did477054694 2-1=#false',  
            'cmd2': 'python ..\MiService\micli.py -did477054694 2-1=#true',  
            'cmd3': 'python ..\MiService\micli.py -did434455491 2-2=#0',#日光
            'cmd4': 'python ..\MiService\micli.py -did434455491 2-2=#1',  
            # 添加更多命令...  
        }  

        # 从字典中获取命令  
        command = cmd_dict.get(cmd)  

        # 如果命令存在，执行它  
        if command:  
            print(f"Exec iot command...")
            result = subprocess.run(command, shell=True)  
        else:  
            print(f'unknown command: {cmd}')  
            
    async def synthesize(self, lang: str, text_stream: AsyncIterator[str]) -> None:
        async for text in text_stream:
            print(f"miText: {text}")
            # sentences = re.split('@', text) 
            # 使用正则表达式找到所有的命令  
            commands = re.findall(r'@', text)
            
            # 使用命令分割文本  
            
            sentences = re.split(r'@', text) 
            for sentence in sentences:  
                if sentence:  # 这个判断可以避免打印空的句子  
                    print(f"sentence: {sentence}") 
                    if sentence.startswith("cmd"):
                      await self.run_cmd(sentence)
                    else:
                      await self.say(sentence)
                      await self.wait_for_duration(calculate_tts_elapse(sentence))
            

            
