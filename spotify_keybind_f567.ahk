#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^F5::
Send, {Media_Prev}
return

^F6::
Send, {Media_Play_Pause}
return

^F7::
Send, {Media_Next}
return