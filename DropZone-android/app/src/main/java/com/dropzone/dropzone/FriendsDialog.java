package com.dropzone.dropzone;

import android.app.AlertDialog;
import android.app.Dialog;
import android.os.Bundle;
import android.support.v4.app.DialogFragment;
import android.widget.ListView;

/**
 * Created by eddie_000 on 1/18/2015.
 */
public class FriendsDialog extends DialogFragment {
    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {



        AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
        builder.setTitle("Choose recipients");
//        builder.setItems()

//        builder.setTitle(getArguments().getInt("title") + "").setView(v);

        return builder.create();
    }
}
