package com.dropzone.dropzone.dropscreens;

import android.app.Activity;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.dropzone.dropzone.MainActivity;
import com.dropzone.dropzone.POSTCallback;
import com.dropzone.dropzone.R;

import org.apache.http.HttpResponse;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

/**
 * Created by eddie_000 on 1/17/2015.
 */
public class TextDrop extends Fragment implements IDropper {
    EditText text;
    MainActivity mainActivity;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_text_drop, container, false);
        text = (EditText) rootView.findViewById(R.id.text_to_drop);
//        Button dropButton = (Button) rootView.findViewById(R.id.button_drop);
//
//        dropButton.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//            }
//        });
        return rootView;
    }

    public void drop() {
        if (mainActivity.dbUserId == -1) {
            Toast.makeText(mainActivity, "User login error", Toast.LENGTH_SHORT).show();
            return;
        }
        Location location = mainActivity.locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
        if (location == null)
            location = mainActivity.locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);

        JSONObject payload = new JSONObject();
        try {
            payload.put("lat", location.getLatitude());
            payload.put("lng", location.getLongitude());
            payload.put("user_id", mainActivity.dbUserId);
            payload.put("data_type", "text");
            payload.put("restrictions", "public");
            payload.put("data_payload", text.getText().toString());
            payload.put("teaser", "TEASER_PLACEHOLDER");
            payload.put("viewcap", "10");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        Log.e("json", payload.toString());
        MainActivity.sendJson(mainActivity.httpClient, "http://dropzone.herokuapp.com/api/drop", payload, new POSTCallback() {

            @Override
            public void onResponse(HttpResponse response) {
                try {
                    JSONObject json = new JSONObject(EntityUtils.toString(response.getEntity()));
                    Log.i("POST response", json.toString());
                } catch (JSONException | IOException e) {
                    e.printStackTrace();
                }
                Toast.makeText(getActivity(), "DROP response received", Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        mainActivity = (MainActivity) activity;
    }
}
