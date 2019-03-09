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
	
	
	ChatSizer->Add( SendSizer, 1, wxEXPAND|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
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
