package com.dropzone.dropzone;

import android.util.Log;

import com.google.android.gms.maps.model.LatLng;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by eddie_000 on 1/17/2015.
 */
public class DropItem {
    public String teaser;
    public double lat, lng;
    private LatLng latLng;
    public int id, user_id;
    public String data_payload;
    public String data_type; // enum
    public String name, photo;
    public boolean close = false;

    public DropItem(JSONObject json) throws JSONException {
        Log.i("dropitem format", json.toString());
        teaser = json.getString("teaser");
        lat = json.getDouble("lat");
        lng = json.getDouble("lng");
        id = json.getInt("id");
        user_id = json.getInt("user_id");
        data_payload = json.getString("data_payload");
        data_type = json.getString("data_type");
        name = json.getString("name");
        photo = json.getString("photo");

        latLng = new LatLng(lat, lng);
//        payload.put("lat", location.getLatitude());
//        payload.put("lng", location.getLongitude());
//        payload.put("user_id", mainActivity.dbUserId);
//        payload.put("data_type", "text");
//        payload.put("restrictions", "public");
//        payload.put("data_payload", text.getText().toString());
//        payload.put("teaser", "TEASER_PLACEHOLDER");
//        payload.put("viewcap", "10")
    }

    public LatLng getLatLng() {
        return latLng;
    }

    public long getId() {
        return id;
    }
}