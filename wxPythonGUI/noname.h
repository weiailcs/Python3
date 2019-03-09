///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/sizer.h>
#include <wx/button.h>
#include <wx/statbox.h>
#include <wx/frame.h>
#include <wx/dialog.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class LoginFrame
///////////////////////////////////////////////////////////////////////////////
class LoginFrame : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* UserNameText;
		wxTextCtrl* UserName;
		wxStaticText* PassWordText;
		wxTextCtrl* PassWord;
		wxButton* Accept;
		
		// Virtual event handlers, overide them in your derived class
		virtual void submmit( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		LoginFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 300,200 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~LoginFrame();
	
};

///////////////////////////////////////////////////////////////////////////////
/// Class FriendListFrame
///////////////////////////////////////////////////////////////////////////////
class FriendListFrame : public wxFrame 
{
	private:
	
	protected:
		wxButton* button_1;
		wxButton* button_2;
		wxButton* button_3;
		wxButton* button__modify;
		
		// Virtual event handlers, overide them in your derived class
		virtual void button_1_clicked( wxCommandEvent& event ) { event.Skip(); }
		virtual void button_2_clicked( wxCommandEvent& event ) { event.Skip(); }
		virtual void button_3_clicked( wxCommandEvent& event ) { event.Skip(); }
		virtual void button_modify_clicked( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		FriendListFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("联系人"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 240,600 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~FriendListFrame();
	
};

///////////////////////////////////////////////////////////////////////////////
/// Class ChatDialog
///////////////////////////////////////////////////////////////////////////////
class ChatDialog : public wxDialog 
{
	private:
	
	protected:
		wxTextCtrl* in_textCtrl;
		wxTextCtrl* out_textCtrl;
		wxButton* send_button;
		
		// Virtual event handlers, overide them in your derived class
		virtual void send_button_clicked( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		ChatDialog( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 579,545 ), long style = wxDEFAULT_DIALOG_STYLE ); 
		~ChatDialog();
	
};

#endif //__NONAME_H__
