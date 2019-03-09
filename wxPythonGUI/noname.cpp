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
