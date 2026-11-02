gBattleAnimMove_SakuraStorm::
	createvisualtask AnimTask_BlendBattleAnimPal, 10, F_PAL_BG, 2, 0, 5, RGB(31, 20, 26)
	playsewithpan SE_M_PETAL_DANCE, SOUND_PAN_ATTACKER
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 0, 30, 24, 50
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 146, 26, 30, 48
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 36, 32, 18, 46
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 182, 28, 34, 44
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 73, 30, 22, 42
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 219, 26, 28, 40
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 109, 32, 20, 38
	playsewithpan SE_M_PETAL_DANCE, SOUND_PAN_TARGET
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 18, 28, 32, 36
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 164, 30, 24, 34
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 55, 26, 30, 32
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 201, 32, 18, 30
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 91, 28, 34, 28
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 237, 30, 22, 26
	delay 2
	createsprite gSakuraPetalSpriteTemplate, ANIM_TARGET, 2, 127, 26, 28, 24
	delay 2
	delay 45
	playsewithpan SE_M_COMET_PUNCH, SOUND_PAN_TARGET
	createvisualtask AnimTask_BlendBattleAnimPal, 10, F_PAL_TARGET, 0, 14, 0, RGB(31, 26, 29)
	createvisualtask AnimTask_ShakeMon2, 2, ANIM_TARGET, 2, 0, 10, 1
	waitforvisualfinish
	createvisualtask AnimTask_BlendBattleAnimPal, 10, F_PAL_BG, 2, 5, 0, RGB(31, 20, 26)
	waitforvisualfinish
	end
