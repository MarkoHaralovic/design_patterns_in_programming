.file	"task6.cpp"
	.intel_syntax noprefix
	.section	.text$Base::Base(),"x"
	.linkonce discard
	.align 2
	.globl	_Base::Base()
	.def	_Base::Base();	.scl	2;	.type	32;	.endef
_Base::Base():
LFB13:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	sub	esp, 24
	mov	DWORD PTR [ebp-12], ecx
	mov	edx, OFFSET FLAT:_vtable for Base 8
	mov	eax, DWORD PTR [ebp-12]
	mov	DWORD PTR [eax], edx
	mov	eax, DWORD PTR [ebp-12]
	mov	ecx, eax
	call	_Base::metoda()
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.section .rdata,"dr"
LC0:
	.ascii "ja sam bazna implementacija!\0"
	.section	.text$Base::virtualnaMetoda(),"x"
	.linkonce discard
	.align 2
	.globl	_Base::virtualnaMetoda()
	.def	_Base::virtualnaMetoda();	.scl	2;	.type	32;	.endef
_Base::virtualnaMetoda():
LFB15:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	sub	esp, 40
	mov	DWORD PTR [ebp-12], ecx
	mov	DWORD PTR [esp], OFFSET FLAT:LC0
	call	_puts
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE15:
	.section .rdata,"dr"
LC1:
	.ascii "Metoda kaze: \0"
	.section	.text$Base::metoda(),"x"
	.linkonce discard
	.align 2
	.globl	_Base::metoda()
	.def	_Base::metoda();	.scl	2;	.type	32;	.endef
_Base::metoda():
LFB16:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	sub	esp, 40
	mov	DWORD PTR [ebp-12], ecx
	mov	DWORD PTR [esp], OFFSET FLAT:LC1
	call	_printf
	mov	eax, DWORD PTR [ebp-12]
	mov	eax, DWORD PTR [eax]
	mov	eax, DWORD PTR [eax]
	mov	edx, DWORD PTR [ebp-12]
	mov	ecx, edx
	call	eax
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE16:
	.section	.text$Derived::Derived(),"x"
	.linkonce discard
	.align 2
	.globl	_Derived::Derived()
	.def	_Derived::Derived();	.scl	2;	.type	32;	.endef
_Derived::Derived():
LFB19:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	sub	esp, 24
	mov	DWORD PTR [ebp-12], ecx
	mov	eax, DWORD PTR [ebp-12]
	mov	ecx, eax
	call	_Base::Base()
	mov	edx, OFFSET FLAT:_vtable for Derived 8
	mov	eax, DWORD PTR [ebp-12]
	mov	DWORD PTR [eax], edx
	mov	eax, DWORD PTR [ebp-12]
	mov	ecx, eax
	call	_Base::metoda()
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE19:
	.section .rdata,"dr"
	.align 4
LC2:
	.ascii "ja sam izvedena implementacija!\0"
	.section	.text$Derived::virtualnaMetoda(),"x"
	.linkonce discard
	.align 2
	.globl	_Derived::virtualnaMetoda()
	.def	_Derived::virtualnaMetoda();	.scl	2;	.type	32;	.endef
_Derived::virtualnaMetoda():
LFB20:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	sub	esp, 40
	mov	DWORD PTR [ebp-12], ecx
	mov	DWORD PTR [esp], OFFSET FLAT:LC2
	call	_puts
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE20:
	.def	___main;	.scl	2;	.type	32;	.endef
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB21:
	.cfi_startproc
	.cfi_personality 0,___gxx_personality_v0
	.cfi_lsda 0,LLSDA21
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	push	esi
	push	ebx
	and	esp, -16
	sub	esp, 32
	.cfi_offset 6, -12
	.cfi_offset 3, -16
	call	___main
	mov	DWORD PTR [esp], 4
LEHB0:
	call	_operator new(unsigned int)
LEHE0:
	mov	ebx, eax
	mov	ecx, ebx
LEHB1:
	call	_Derived::Derived()
LEHE1:
	mov	DWORD PTR [esp 28], ebx
	mov	eax, DWORD PTR [esp 28]
	mov	ecx, eax
LEHB2:
	call	_Base::metoda()
	mov	eax, 0
	jmp	L10
L9:
	mov	esi, eax
	mov	DWORD PTR [esp 4], 4
	mov	DWORD PTR [esp], ebx
	call	_operator delete(void*, unsigned int)
	mov	eax, esi
	mov	DWORD PTR [esp], eax
	call	__Unwind_Resume
LEHE2:
L10:
	lea	esp, [ebp-8]
	pop	ebx
	.cfi_restore 3
	pop	esi
	.cfi_restore 6
	pop	ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE21:
	.def	___gxx_personality_v0;	.scl	2;	.type	32;	.endef
	.section	.gcc_except_table,"w"
LLSDA21:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 LLSDACSE21-LLSDACSB21
LLSDACSB21:
	.uleb128 LEHB0-LFB21
	.uleb128 LEHE0-LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 LEHB1-LFB21
	.uleb128 LEHE1-LEHB1
	.uleb128 L9-LFB21
	.uleb128 0
	.uleb128 LEHB2-LFB21
	.uleb128 LEHE2-LEHB2
	.uleb128 0
	.uleb128 0
LLSDACSE21:
	.text
	.globl	_vtable for Derived
	.section	.rdata$vtable for Derived,"dr"
	.linkonce same_size
	.align 4
_vtable for Derived:
	.long	0
	.long	_typeinfo for Derived
	.long	_Derived::virtualnaMetoda()
	.globl	_vtable for Base
	.section	.rdata$vtable for Base,"dr"
	.linkonce same_size
	.align 4
_vtable for Base:
	.long	0
	.long	_typeinfo for Base
	.long	_Base::virtualnaMetoda()
	.globl	_typeinfo for Derived
	.section	.rdata$typeinfo for Derived,"dr"
	.linkonce same_size
	.align 4
_typeinfo for Derived:
	.long	_vtable for __cxxabiv1::__si_class_type_info 8
	.long	_typeinfo name for Derived
	.long	_typeinfo for Base
	.globl	_typeinfo name for Derived
	.section	.rdata$typeinfo name for Derived,"dr"
	.linkonce same_size
	.align 4
_typeinfo name for Derived:
	.ascii "7Derived\0"
	.globl	_typeinfo for Base
	.section	.rdata$typeinfo for Base,"dr"
	.linkonce same_size
	.align 4
_typeinfo for Base:
	.long	_vtable for __cxxabiv1::__class_type_info 8
	.long	_typeinfo name for Base
	.globl	_typeinfo name for Base
	.section	.rdata$typeinfo name for Base,"dr"
	.linkonce same_size
	.align 4
_typeinfo name for Base:
	.ascii "4Base\0"
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_puts;	.scl	2;	.type	32;	.endef
	.def	_printf;	.scl	2;	.type	32;	.endef
	.def	_operator new(unsigned int);	.scl	2;	.type	32;	.endef
	.def	_operator delete(void*, unsigned int);	.scl	2;	.type	32;	.endef
	.def	__Unwind_Resume;	.scl	2;	.type	32;	.endef