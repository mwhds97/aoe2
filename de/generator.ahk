#SingleInstance, Force
SetTitleMatchMode, RegEx
CoordMode, Mouse, Screen
SendMode Input

title_1 := "Advanced Genie Editor"
title_2 := "AGE.+window 2"
tab_techs := [20, 85]
tab_effects := [65, 85]
tab_techtrees := [120, 85]
tab_techtrees_ages := [30, 185]
tab_techtrees_buildings := [80, 185]
tab_techtrees_techs := [175, 185]
btn_left_add := [88, 1008]
btn_left_delete := [238, 1008]
btn_left_copy := [88, 1032]
btn_left_paste := [238, 1032]
btn_effects_commands_add := [615, 980]
btn_effects_commands_delete := [840, 980]
btn_techtrees_ages_buildings_add := [555, 480]
btn_techtrees_ages_buildings_delete := [715, 480]
btn_techtrees_ages_techs_add := [1515, 480]
btn_techtrees_ages_techs_copy := [1515, 505]
btn_techtrees_ages_techs_paste := [1675, 505]
btn_techtrees_buildings_techs_add := [1515, 505]
btn_techtrees_buildings_techs_copy := [1515, 530]
btn_techtrees_buildings_techs_paste := [1675, 530]
input_techs_effects_left := [360, 130]
input_effects_commands := [1065, 225]
input_effects_commandtype := [1260, 130]
input_effects_attributes := [1400, 360]
input_techtrees_left := [380, 205]
input_techtrees_ages_buildings_above := [900, 275]
input_techtrees_ages_buildings_below := [900, 430]
input_techtrees_buildings_linemode := [920, 230]
input_techtrees_buildings_items := [900, 800]
input_techtrees_buildings_totalunits_above := [1165, 605]
input_techtrees_buildings_totalunits_below := [1165, 655]
rows_techs_left := [200, 230]
rows_effects_left := [200, 180]
rows_effects_commands := [800, 275]
rows_techtrees_left := [200, 305]
rows_techtrees_ages_techs := [1650, 325]
rows_techtrees_buildings_techs := [1650, 350]
rows_techtrees_buildings_items := [700, 695]

_click(pos, count := 1, delay := 50) {
  Loop, %count% {
    Click, % pos[1] "," pos[2]
    Sleep, 50
  }
  Sleep, %delay%
}

_send(key, count := 1, delay := 50) {
  Loop, %count% {
    Send, %key%
    Sleep, 50
  }
  Sleep, %delay%
}

shift_repeat(key, count) {
  _send("{Shift Down}")
  _send(key, count, 0)
  _send("{Shift Up}")
}

clear_input(pos) {
  _click(pos)
  _send("^a")
  _send("{BackSpace}")
}

WinSet, Style, -0xC40000, %title_1%
WinMove, %title_1%,, 0, 0, 1920, 1080
WinSet, Style, -0xC40000, %title_2%
WinMove, %title_2%,, 0, 0, 1920, 1080
Return

F1::
;New Effects
WinActivate, %title_2%
Sleep, 1000
_click(tab_effects,, 950)
_click(rows_effects_left)
_send("{End}")
shift_repeat("{Up}", 11)
_click(btn_left_copy)
WinActivate, %title_1%
Sleep, 1000
_click(tab_effects,, 950)
_click(btn_left_add, 200)
_click(input_techs_effects_left)
_send("901")
_click(btn_left_paste)
clear_input(input_techs_effects_left)
_send("913")
clear_input(input_techs_effects_left)
_click(rows_effects_left)
shift_repeat("{End}", 1)
_click(btn_left_delete)
;New Techs
WinActivate, %title_2%
Sleep, 1000
_click(tab_techs,, 950)
_click(rows_techs_left)
_send("{End}")
shift_repeat("{Up}", 11)
_click(btn_left_copy)
WinActivate, %title_1%
Sleep, 1000
_click(tab_techs,, 950)
_click(btn_left_add, 200)
_click(input_techs_effects_left)
_send("901")
_click(btn_left_paste)
clear_input(input_techs_effects_left)
_send("913")
clear_input(input_techs_effects_left)
_click(rows_techs_left)
shift_repeat("{End}", 1)
_click(btn_left_delete)
;Tech Trees
WinActivate, %title_2%
Sleep, 1000
_click(tab_techtrees,, 950)
_click(tab_techtrees_techs,, 950)
_click(rows_techtrees_left)
_send("{End}")
shift_repeat("{Up}", 11)
_click(btn_left_copy)
WinActivate, %title_1%
Sleep, 1000
_click(tab_techtrees,, 950)
_click(tab_techtrees_techs,, 950)
_click(btn_left_add)
_click(btn_left_paste)
WinActivate, %title_2%
Sleep, 1000
_click(tab_techtrees_ages,, 950)
_click(rows_techtrees_left)
_send("{End}")
_click(rows_techtrees_ages_techs)
_send("{End}")
shift_repeat("{Up}", 11)
_click(btn_techtrees_ages_techs_copy)
WinActivate, %title_1%
Sleep, 1000
_click(tab_techtrees_ages,, 950)
_click(rows_techtrees_left)
_send("{End}")
_click(btn_techtrees_ages_techs_add)
_click(btn_techtrees_ages_techs_paste)
_click(input_techtrees_ages_buildings_above)
_send("276")
_click(btn_techtrees_ages_buildings_delete)
_click(rows_techtrees_left)
_send("{End}")
_send("{Up}")
clear_input(input_techtrees_ages_buildings_above)
_click(btn_techtrees_ages_buildings_add)
clear_input(input_techtrees_ages_buildings_below)
_send("276")
_send("{Enter}")
WinActivate, %title_2%
Sleep, 1000
_click(tab_techtrees_buildings,, 950)
_click(input_techtrees_left)
_send("276")
_click(rows_techtrees_buildings_techs)
shift_repeat("{End}", 1)
_click(btn_techtrees_buildings_techs_copy)
WinActivate, %title_1%
Sleep, 1000
_click(tab_techtrees_buildings,, 950)
_click(input_techtrees_left)
_send("276")
clear_input(input_techtrees_buildings_linemode)
_send("5")
_click(btn_techtrees_buildings_techs_add)
_click(btn_techtrees_buildings_techs_paste)
_click(rows_techtrees_buildings_items)
clear_input(input_techtrees_buildings_items)
_send("3")
clear_input(input_techtrees_buildings_totalunits_above)
_send("12")
clear_input(input_techtrees_buildings_totalunits_below)
_send("6")
;Mod Effects
_click(tab_effects,, 950)
_click(input_techs_effects_left)
_send("215")
clear_input(input_effects_attributes)
_send("-150")
clear_input(input_techs_effects_left)
_send("254")
_click(input_effects_commands)
_send("disable tech 437")
_click(btn_effects_commands_delete)
clear_input(input_techs_effects_left)
_send("256")
clear_input(input_effects_commands)
_send("disable tech 75")
_click(btn_effects_commands_delete)
clear_input(input_effects_commands)
_send("disable tech 435")
_click(btn_effects_commands_delete)
clear_input(input_techs_effects_left)
_send("257")
clear_input(input_effects_commands)
_send("disable tech 12")
_click(btn_effects_commands_delete)
clear_input(input_effects_commands)
_send("disable tech 188")
_click(btn_effects_commands_delete)
clear_input(input_effects_commands)
_send("disable tech 377")
_click(btn_effects_commands_delete)
clear_input(input_techs_effects_left)
_send("258")
clear_input(input_effects_commands)
_send("disable tech 435")
_click(btn_effects_commands_delete)
clear_input(input_techs_effects_left)
_send("276")
clear_input(input_effects_commands)
_send("disable tech 373")
_click(btn_effects_commands_delete)
clear_input(input_techs_effects_left)
_send("447")
clear_input(input_effects_commands)
_send("disable tech 429")
_click(btn_effects_commands_delete)
clear_input(input_techs_effects_left)
_send("448")
clear_input(input_effects_commands)
_click(btn_effects_commands_add)
clear_input(input_effects_commandtype)
_send("102")
_send("{Enter}")
clear_input(input_effects_attributes)
_send("265")
clear_input(input_techs_effects_left)
_send("449")
_click(input_effects_commands)
_send("disable tech 264")
_click(btn_effects_commands_delete)
Return

F2::
techtrees := ["1", "3", "5", "7", "10", "31", "37", "42", "48", "254", "255", "256", "257", "258", "259", "260", "261", "262", "263", "275", "276", "277", "446", "447", "448", "449", "504", "646", "648", "650", "652", "706", "708", "710", "712", "782", "784", "801", "803"]
Loop, % techtrees.Length() {
  clear_input(input_techs_effects_left)
  _send(techtrees[A_Index])
  clear_input(input_effects_commands)
  _send("disable tech")
  _click(rows_effects_commands)
  shift_repeat("{End}", 1)
  _click(btn_effects_commands_delete)
  clear_input(input_effects_commands)
  _click(btn_effects_commands_add)
  clear_input(input_effects_commandtype)
  _send("102")
  _send("{Enter}")
  clear_input(input_effects_attributes)
  _send("291")
  _click(btn_effects_commands_add)
  clear_input(input_effects_commandtype)
  _send("102")
  _send("{Enter}")
  clear_input(input_effects_attributes)
  _send("293")
  _click(btn_effects_commands_add)
  clear_input(input_effects_commandtype)
  _send("102")
  _send("{Enter}")
  clear_input(input_effects_attributes)
  _send("294")
  _click(btn_effects_commands_add)
  clear_input(input_effects_commandtype)
  _send("102")
  _send("{Enter}")
  clear_input(input_effects_attributes)
  _send("338")
  _click(btn_effects_commands_add)
  clear_input(input_effects_commandtype)
  _send("102")
  _send("{Enter}")
  clear_input(input_effects_attributes)
  _send("356")
}
_send("{Enter}")
Return

^LButton::
MouseGetPos, X, Y
MsgBox, % X "," Y
Return

Esc::
ExitApp
Return
