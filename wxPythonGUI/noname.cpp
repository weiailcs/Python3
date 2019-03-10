///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

LoginFrame::LoginFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxStaticBoxSizer* LoginSize;
	LoginSize = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("登录") ), wxVERTICAL );
	
	LoginSize->SetMinSize( wxSize( 300,150 ) ); 
	wxGridSizer* gSizer1;
	gSizer1 = new wxGridSizer( 0, 2, 0, 0 );
	
	UserNameText = new wxStaticText( LoginSize->GetStaticBox(), wxID_ANY, wxT("账号"), wxDefaultPosition, wxDefaultSize, 0 );
	UserNameText->Wrap( -1 );
	gSizer1->Add( UserNameText, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	UserName = new wxTextCtrl( LoginSize->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	UserName->SetMinSize( wxSize( 250,24 ) );
	
	gSizer1->Add( UserName, 0, wxALL, 5 );
	
	PassWordText = new wxStaticText( LoginSize->GetStaticBox(), wxID_ANY, wxT("密码"), wxDefaultPosition, wxDefaultSize, 0 );
	PassWordText->Wrap( -1 );
	gSizer1->Add( PassWordText, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	PassWord = new wxTextCtrl( LoginSize->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	PassWord->SetMinSize( wxSize( 250,24 ) );
	
	gSizer1->Add( PassWord, 0, wxALL, 5 );
	
	
	LoginSize->Add( gSizer1, 1, wxEXPAND, 5 );
	
	Accept = new wxButton( LoginSize->GetStaticBox(), wxID_ANY, wxT("确定"), wxDefaultPosition, wxDefaultSize, 0 );
	LoginSize->Add( Accept, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	this->SetSizer( LoginSize );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	Accept->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( LoginFrame::submmit ), NULL, this );
}

LoginFrame::~LoginFrame()
{
	// Disconnect Events
	Accept->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( LoginFrame::submmit ), NULL, this );
	
}

ModifyFrame::ModifyFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxStaticBoxSizer* ModifySize;
	ModifySize = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("修改密码") ), wxVERTICAL );
	
	ModifySize->SetMinSize( wxSize( 300,150 ) ); 
	wxGridSizer* ModifySizer;
	ModifySizer = new wxGridSizer( 0, 2, 0, 0 );
	
	PassWordText = new wxStaticText( ModifySize->GetStaticBox(), wxID_ANY, wxT("密码"), wxDefaultPosition, wxDefaultSize, 0 );
	PassWordText->Wrap( -1 );
	ModifySizer->Add( PassWordText, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	PassWord = new wxTextCtrl( ModifySize->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	PassWord->SetMinSize( wxSize( 250,24 ) );
	
	ModifySizer->Add( PassWord, 0, wxALL, 5 );
	
	CheckPassWordText = new wxStaticText( ModifySize->GetStaticBox(), wxID_ANY, wxT("确认密码"), wxDefaultPosition, wxDefaultSize, 0 );
	CheckPassWordText->Wrap( -1 );
	ModifySizer->Add( CheckPassWordText, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	CheckPassWord = new wxTextCtrl( ModifySize->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	CheckPassWord->SetMinSize( wxSize( 250,24 ) );
	
	ModifySizer->Add( CheckPassWord, 0, wxALL, 5 );
	
	
	ModifySize->Add( ModifySizer, 1, wxEXPAND, 5 );
	
	Accept = new wxButton( ModifySize->GetStaticBox(), wxID_ANY, wxT("确定"), wxDefaultPosition, wxDefaultSize, 0 );
	ModifySize->Add( Accept, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	this->SetSizer( ModifySize );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	Accept->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModifyFrame::submmit ), NULL, this );
}

ModifyFrame::~ModifyFrame()
{
	// Disconnect Events
	Accept->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ModifyFrame::submmit ), NULL, this );
	
}

FriendListFrame::FriendListFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxSize( 240,600 ) );
	
	wxBoxSizer* FriendListSizer;
	FriendListSizer = new wxBoxSizer( wxVERTICAL );
	
	FriendListSizer->SetMinSize( wxSize( 160,200 ) ); 
	button_1 = new wxButton( this, wxID_ANY, wxT("陈浩（20171001091）"), wxDefaultPosition, wxDefaultSize, 0 );
	FriendListSizer->Add( button_1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	button_2 = new wxButton( this, wxID_ANY, wxT("2"), wxDefaultPosition, wxDefaultSize, 0 );
	FriendListSizer->Add( button_2, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	button_3 = new wxButton( this, wxID_ANY, wxT("3"), wxDefaultPosition, wxDefaultSize, 0 );
	FriendListSizer->Add( button_3, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	FriendListSizer->Add( 0, 0, 1, wxEXPAND|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	button__modify = new wxButton( this, wxID_ANY, wxT("修改密码"), wxDefaultPosition, wxDefaultSize, 0 );
	FriendListSizer->Add( button__modify, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	this->SetSizer( FriendListSizer );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	button_1->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_1_clicked ), NULL, this );
	button_2->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_2_clicked ), NULL, this );
	button_3->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_3_clicked ), NULL, this );
	button__modify->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_modify_clicked ), NULL, this );
}

FriendListFrame::~FriendListFrame()
{
	// Disconnect Events
	button_1->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_1_clicked ), NULL, this );
	button_2->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_2_clicked ), NULL, this );
	button_3->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_3_clicked ), NULL, this );
	button__modify->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( FriendListFrame::button_modify_clicked ), NULL, this );
	
}

ChatDialog::ChatDialog( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxDialog( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxStaticBoxSizer* ChatSizer;
	ChatSizer = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("label") ), wxVERTICAL );
	
	in_textCtrl = new wxTextCtrl( ChatSizer->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 400,300 ), 0|wxVSCROLL );
	ChatSizer->Add( in_textCtrl, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	wxBoxSizer* SendSizer;
	SendSizer = new wxBoxSizer( wxHORIZONTAL );
	
	out_textCtrl = new wxTextCtrl( ChatSizer->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 300,100 ), 0 );
	SendSizer->Add( out_textCtrl, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	send_button = new wxButton( ChatSizer->GetStaticBox(), wxID_ANY, wxT("发送"), wxDefaultPosition, wxDefaultSize, 0 );
	SendSizer->Add( send_button, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	ChatSizer->Add( SendSizer, 1, wxEXPAND|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 );
	
	
	this->SetSizer( ChatSizer );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	send_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ChatDialog::send_button_clicked ), NULL, this );
}

ChatDialog::~ChatDialog()
{
	// Disconnect Events
	send_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( ChatDialog::send_button_clicked ), NULL, this );
	
}

MenuFrame::MenuFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxVERTICAL );
	
	bSizer3->SetMinSize( wxSize( 200,160 ) ); 
	wxBoxSizer* bSizer4;
	bSizer4 = new wxBoxSizer( wxHORIZONTAL );
	
	bSizer4->SetMinSize( wxSize( 200,160 ) ); 
	friend_name = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer4->Add( friend_name, 0, wxALL, 5 );
	
	search_button = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer4->Add( search_button, 0, wxALL, 5 );
	
	
	bSizer3->Add( bSizer4, 1, wxEXPAND, 5 );
	
	button_modify = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer3->Add( button_modify, 0, wxALL, 5 );
	
	
	this->SetSizer( bSizer3 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	search_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MenuFrame::search_button_clicked ), NULL, this );
	button_modify->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MenuFrame::button_modify_clicked ), NULL, this );
}

MenuFrame::~MenuFrame()
{
	// Disconnect Events
	search_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MenuFrame::search_button_clicked ), NULL, this );
	button_modify->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MenuFrame::button_modify_clicked ), NULL, this );
	
}
