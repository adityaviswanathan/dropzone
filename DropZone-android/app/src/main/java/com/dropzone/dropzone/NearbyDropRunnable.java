package com.dropzone.dropzone;

import android.location.Location;
import android.os.AsyncTask;
import android.util.Log;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.model.MarkerOptions;

import org.apache.http.HttpResponse;
import org.apache.http.StatusLine;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;

/**
 * Created by eddie_000 on 1/17/2015.
 */
public class NearbyDropRunnable implements Runnable {
    MapsFragment mapsFragment;
    HttpGet nearbyDropsGet;
    HashSet<Integer> dropIds;

    public NearbyDropRunnable(MapsFragment mapsFragment, HttpGet nearbyDropsGet) {
        this.mapsFragment = mapsFragment;
        this.nearbyDropsGet = nearbyDropsGet;
        dropIds = new HashSet<>();
    }

    @Override
    public void run() {
        // Kill me
        try {
            HttpResponse response = mapsFragment.mainActivity.httpClient.execute(nearbyDropsGet);

            if (response != null) {
                StatusLine status = response.getStatusLine();
                if (status.getStatusCode() != 200) {
                    Log.e("NEARBY DROPS GET", status.toString());
                    return;
                }
                JSONArray json = new JSONObject(EntityUtils.toString(response.getEntity())).getJSONArray("drops");
                Log.i("NEARBY DROPS GET", status.toString());
                final ArrayList<DropItem> newDrops = new ArrayList<>();
                for (int i = 0; i < json.length(); i++) {
                    JSONObject drop = json.getJSONObject(i);
                    if (dropIds.contains(drop.getInt("id")))
                        continue;
                    else {
                        dropIds.add(drop.getInt("id"));
                        newDrops.add(new DropItem(drop));
                    }
                }
                mapsFragment.mainActivity.runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        DropAdapter dropAdapter = (DropAdapter) mapsFragment.dropList.getAdapter();
                        dropAdapter.addAll(newDrops);
                        Location loc = mapsFragment.map.getMyLocation();
                        for (DropItem drop : newDrops) {
                            mapsFragment.map.addMarker(new MarkerOptions().position(drop.getLatLng()));
                        }
                        for (int i = 0; i < dropAdapter.getCount(); i++) {
                            DropItem drop = dropAdapter.getItem(i);
                            float[] dist = new float[1];
                            Location.distanceBetween(drop.lat, drop.lng, loc.getLatitude(), loc.getLongitude(), dist);
                            if (dist[0] < 10) {
                                // TODO:
                                Log.i("Close drop", "ID: " + drop.getId());
                                drop.close = true;
                            }
                            else {
                                drop.close = false;
                            }
                        }
                        dropAdapter.notifyDataSetChanged();
                    }
                });
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
