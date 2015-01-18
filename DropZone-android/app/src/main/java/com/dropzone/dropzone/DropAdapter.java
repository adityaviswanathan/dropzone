package com.dropzone.dropzone;

import android.app.AlertDialog;
import android.content.Context;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.location.Location;
import android.os.AsyncTask;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ListAdapter;
import android.widget.TextView;

import org.apache.http.HttpRequest;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.util.EntityUtils;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by eddie_000 on 1/17/2015.
 */
public class DropAdapter extends ArrayAdapter<DropItem> {
    MainActivity mainActivity;

    public DropAdapter(MainActivity mainActivity) {
        super(mainActivity, R.layout.drop_list_item);
        this.mainActivity = mainActivity;
    }

    @Override
    public View getView(final int position, final View convertView, ViewGroup parent) {
//        ViewHolder holder = new ViewHolder();
//        holder.icon = (ImageView) convertView.findViewById(R.id.listitem_image);
//        holder.text = (TextView) convertView.findViewById(R.id.listitem_text);
//        holder.timestamp = (TextView) convertView.findViewById(R.id.listitem_timestamp);
//        holder.progress = (ProgressBar) convertView.findViewById(R.id.progress_spinner);
//        convertView.setTag(holder);
        LayoutInflater inflater = (LayoutInflater) mainActivity
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        final View dropView = inflater.inflate(R.layout.drop_list_item, parent, false);
        ImageView submitterPicture = (ImageView) dropView.findViewById(R.id.submitter_icon);
        TextView dropType = (TextView) dropView.findViewById(R.id.type_view);
        final TextView submitterName = (TextView) dropView.findViewById(R.id.submitter_name);
        TextView dist = (TextView) dropView.findViewById(R.id.drop_dist);
        dropType.setText(firstToUpper(getItem(position).data_type));
        submitterName.setText(getItem(position).name);
        dropView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!getItem(position).close)
                    return;
                AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(getContext());
                dialogBuilder.setMessage(getItem(position).data_payload);
                dialogBuilder.show();
            }
        });
        new ImageDownloader(submitterPicture).execute(getItem(position).photo);
//        final HttpGet userGet = new HttpGet("http://dropzone.heroku.com/api/user/" + getItem(position).user_id);
//        new Thread(new Runnable() {
//            @Override
//            public void run() {
//                try {
//                    HttpResponse response = mainActivity.httpClient.execute(userGet);
//                    final JSONObject json = new JSONObject(EntityUtils.toString(response.getEntity())).getJSONObject("user");
//                    Log.i("User info", json.toString());
//                    mainActivity.runOnUiThread(new Runnable() {
//                        @Override
//                        public void run() {
//                            try {
//                                submitterName.setText(json.getString("name"));
//                                // TODO:
//                            } catch (JSONException e) {
//                                e.printStackTrace();
//                            }
//                        }
//                    });
//                } catch (IOException | JSONException e) {
//                    e.printStackTrace();
//                }
//            }
//        }).start();
        if (getItem(position).close) {
            submitterPicture.setBackgroundColor(0xff41ff23);
        }
//        else {
            if (position % 2 == 0) {
                dropView.setBackgroundColor(0xffdff0f7);
            } else {
                dropView.setBackgroundColor(0xffeff8fb);// TODO:
            }
//        }
        // TODO: icon for text, photo, etc; distance

        return dropView;
    }

    static String firstToUpper(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }

//    static class ViewHolder {
//        ImageView submitterPicture;
//        TextView submitterName;
//    }
}
