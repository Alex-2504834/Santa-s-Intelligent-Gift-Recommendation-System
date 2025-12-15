from __future__ import annotations

import json
import random
import traceback
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional
import customtkinter

@dataclass
class AppSettings:
    appearanceMode: str = "dark"
    colorTheme: str = "blue"

def getSettingsFilePath() -> Path:
    homeDirPath: Path = Path.home()
    docDirPath: Path = homeDirPath / "Documents"
    settingsDirPath: Path = docDirPath / "IGRS"
    settingsDirPath.mkdir(parents=True, exist_ok=True)
    settingsFilePath: Path = settingsDirPath / "settings.json"
    return settingsFilePath

def loadAppSettingsFromDisk() -> AppSettings:
    settingsPath: Path = getSettingsFilePath()

    if not settingsPath.exists():
        return AppSettings()
    
    try:
        with settingsPath.open("r", encoding="utf-8") as settingsFile:
            rawData = json.load(settingsFile)

        return AppSettings(
            appearanceMode=str(rawData.get("appearanceMode", "dark")),
            colorTheme=str(rawData.get("colorTheme", "blue")),
        )
    except Exception as error:
        print("Error loading app settings: ", error)
        traceback.print_exc()
        return AppSettings()

class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Santa's Intelligent Gift Recommendation System")
        self.geometry(f"{500}x{500}")



        

if __name__ == "__main__":
    app = App()
    app.mainloop()